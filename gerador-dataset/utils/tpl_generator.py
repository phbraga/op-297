import numpy as np
def tpl_generator(crmp):
    """
    Funcao que gera o arquivo .tpl com os controles e os tempos de controle
    crmp: dict -> Dicionario com os parametros de entrada para o template
    """
    base_file = crmp["ac1"]
    result_file = base_file.replace(".tpl", "_generated.tpl")
    control_steps = crmp["control_steps"]
    num_prod = crmp["num_prod"]
    num_inj = crmp["num_inj"]
    window_size = crmp["window_size"]
    time_skip = crmp["tpl_time_skip"]
    sim_time = crmp["sim_time"]

    alter_template = "**__________________________________________________\n*ALTER  "
    prod_template = ""
    for i in range(num_prod - 1):
        prod_template += "'P-" + str(i + 1) + "'  "
    prod_template += "'P-" + str(num_prod) + "'\n"
    prod_template = alter_template + prod_template

    inj0_template = ""
    for i in range(num_inj - 1):
        inj0_template += "'I-" + str(i + 1) + "'  "
    inj0_template += "'I-" + str(num_inj) + "'\n"
    inj0_template = alter_template + inj0_template

    if "wag" in crmp.keys() and crmp["wag"]:
        inj1_template = ""
        for i in range(num_inj, num_inj * 2 - 1):
            inj1_template += "'I-" + str(i + 1) + "'  "
        inj1_template += "'I-" + str(num_inj * 2) + "'\n"
        inj1_template = alter_template + inj1_template

        shutin0_template = ""
        for i in range(num_inj):
            shutin0_template += "*SHUTIN  'I-" + str(i + 1) + "' \n"

        shutin1_template = ""
        for i in range(num_inj, num_inj * 2):
            shutin1_template += "*SHUTIN  'I-" + str(i + 1) + "' \n"

    control_strings = []
    control_change_steps = 1
    curr_inj_template = 0
    inj_template = inj0_template
    for i in range(1, control_steps + 1):
        prod_control = "   "
        for j in range(1, num_prod + 1):
            prod_control += f"  $GP{i}_{j}"
        prod_control += "\n"
        inj_control = "   "
        for j in range(1, num_inj + 1):
            inj_control += f"  $GI{i}_{j}"
        inj_control += "\n"

        if "wag" in crmp.keys() and crmp["wag"]:
            if control_change_steps > crmp["npw"]:
                control_change_steps = 1
                if curr_inj_template == 0:
                    inj_template = inj1_template
                    curr_inj_template = 1
                else:
                    inj_template = inj0_template
                    curr_inj_template = 0
            
            control_change_steps += 1
        
        control = prod_template + prod_control + inj_template + inj_control
        control_strings.append(control)


    if isinstance(time_skip, int):
        control_timers = []
        to_divide = sim_time - time_skip
        control_timers.append(time_skip)
        for i in range(1, control_steps):
            control_timers.append(time_skip + int((i / control_steps) * to_divide))

        timer = {}
        timer[crmp['delta_start']] = f"\n*TIME {crmp['delta_start']}\n"
        # print_timers = np.arange(int(time_skip), sim_time, window_size)
        # for time in range(sim_time):
        for time in np.arange(window_size, sim_time, window_size):
            if time in control_timers:
                # timer[time - 1] = "*TIME " + str(time - 1) + "\n"
                timer[time] = "*TIME " + str(time) + "\n"
                timer[time + crmp["delta_start"]] = "*TIME " + str(time + crmp['delta_start']) + "\n"
            else:
                timer[time] = "*TIME " + str(time) + "\n"
        timer[sim_time] = "*TIME " + str(sim_time) + "\n"
    else:
        control_timers = []
        to_divide = sim_time - int(time_skip)
        control_timers.append(time_skip)
        for i in range(1, control_steps):
            control_timers.append(int(time_skip) + int((i / control_steps) * to_divide))

        timer = {}
        timer[crmp['delta_start']] = f"\n*TIME {crmp['delta_start']}\n"
        timer[2 * time_skip] = f"\n*TIME {2 * time_skip}\n"
        print_timers = np.arange(window_size, sim_time, window_size)
        for time in range(sim_time):
        # for time in np.arange(window_size, sim_time, window_size):
            if time in control_timers:
                timer[time] = "*TIME " + str(time) + "\n"
                timer[time + crmp['delta_start']] = "*TIME " + str(time + crmp['delta_start']) + "\n"
            elif time in print_timers:
                timer[time] = "*TIME " + str(time) + "\n"

        if time <= sim_time:
            timer[sim_time - 2] = "*TIME " + str(sim_time - 2) + "\n"
            timer[sim_time - 1] = "*TIME " + str(sim_time - 1) + "\n"
            timer[sim_time] = "*TIME " + str(sim_time) + "\n"

    # Read all base_file and put it in the variable "header"
    with open(base_file, "r") as f:
        header = f.readlines()

    generated_controls = []
    generated_controls_steps = 1
    shutin_template_id = 0
    for time, time_string in timer.items():
        generated_controls.append(time_string)
        if time in control_timers:
            generated_controls.append(control_strings[control_timers.index(time)])
            if "wag" in crmp.keys() and crmp["wag"]:
                if generated_controls_steps > crmp["npw"]:
                    if shutin_template_id == 0:
                        generated_controls.append(shutin0_template)
                        shutin_template_id = 1
                    else:
                        generated_controls.append(shutin1_template)
                        shutin_template_id = 0

                    generated_controls_steps = 1
                
                generated_controls_steps += 1

    generated_controls.append("\n*STOP")

    # Write the new file
    with open(result_file, "w") as f:
        f.writelines(header)
        f.writelines(generated_controls)

    crmp["ac1"] = result_file