*FILE '<file>.sr3'     ** Nome do arquivo de entrada
**LIST-PARAMETERS
*LINES-PER-PAGE 100000000    ** Don't have any page breaks in a table.
*TABLE-WIDTH     150000     ** Produce a wide table if many producers,
*NO-BLANKS               ** Always have a value in every column,
*WIDTH 18
*PRECISION 7            ** with four significant digits.
*TIME ON                 ** The tables will have no time column,
*DATE OFF                ** but will have a date column
*TABLE-FOR
  
			
			
   *COLUMN-FOR  *WELLS 'P-1'
                *PARAMETERS 'BHP' 
                *PARAMETERS 'Liquid Rate RC'
                *PARAMETERS 'Oil Rate SC'  
                *PARAMETERS 'Water Rate RC' 
            

   *COLUMN-FOR  *WELLS 'P-2'
                *PARAMETERS 'BHP' 
                *PARAMETERS 'Liquid Rate RC'
                *PARAMETERS 'Oil Rate SC'  
                *PARAMETERS 'Water Rate RC' 
                   
   *COLUMN-FOR  *WELLS 'P-3'
                *PARAMETERS 'BHP' 
                *PARAMETERS 'Liquid Rate RC'
                *PARAMETERS 'Oil Rate SC'  
                *PARAMETERS 'Water Rate RC' 
                    				
   *COLUMN-FOR  *WELLS 'P-4'
                *PARAMETERS 'BHP' 
                *PARAMETERS 'Liquid Rate RC'
                *PARAMETERS 'Oil Rate SC'  
                *PARAMETERS 'Water Rate RC' 
	
    *COLUMN-FOR  *WELLS 'I-1'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'
    
    *COLUMN-FOR  *WELLS 'I-2'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'
	 			
    *COLUMN-FOR  *WELLS 'I-3'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'

			
    *COLUMN-FOR  *WELLS 'I-4'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'
				
    *COLUMN-FOR *WELLS 'I-5'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'
	 			
    *COLUMN-FOR *WELLS 'I-6'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'
				
     *COLUMN-FOR *WELLS 'I-7'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'
     
	 
	 *COLUMN-FOR *WELLS 'I-8'
	            *PARAMETERS 'BHP' 
     			*PARAMETERS 'Water Rate SC'
			   
			   
*TABLE-END

