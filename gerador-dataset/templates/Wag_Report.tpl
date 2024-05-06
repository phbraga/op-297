*FILE '<file>.sr3'     ** Nome do arquivo de entrada
**LIST-PARAMETERS
*LINES-PER-PAGE 1000000    ** Don't have any page breaks in a table.
*TABLE-WIDTH     1000     ** Produce a wide table if many producers,
*NO-BLANKS               ** Always have a value in every column,
*WIDTH 14
*PRECISION 6            ** with four significant digits.
*TIME ON                 ** The tables will have no time column,
*DATE OFF                ** but will have a date column
*TABLE-FOR



   *COLUMN-FOR  *WELLS 'P-1'
                *PARAMETERS 'BHP'            

   *COLUMN-FOR  *WELLS 'P-1'
                *PARAMETERS 'Liquid Rate RC' 

   *COLUMN-FOR  *WELLS 'P-1'
                *PARAMETERS 'Oil Rate SC'   

   *COLUMN-FOR  *WELLS 'P-1'
                *PARAMETERS 'Water Rate RC'            

   *COLUMN-FOR  *WELLS 'P-2'
                *PARAMETERS 'BHP'
                   
   *COLUMN-FOR  *WELLS 'P-2'
                *PARAMETERS 'Liquid Rate RC'

   *COLUMN-FOR  *WELLS 'P-2'
                *PARAMETERS 'Oil Rate SC'   				

   *COLUMN-FOR  *WELLS 'P-2'
                *PARAMETERS 'Water Rate RC'            
				   
   *COLUMN-FOR  *WELLS 'P-3'
                *PARAMETERS 'BHP'
				
   *COLUMN-FOR  *WELLS 'P-3'
                *PARAMETERS 'Liquid Rate RC'

   *COLUMN-FOR  *WELLS 'P-3'
                *PARAMETERS 'Oil Rate SC'   
                    				
   *COLUMN-FOR  *WELLS 'P-3'
                *PARAMETERS 'Water Rate RC'            

   *COLUMN-FOR  *WELLS 'P-4'
                *PARAMETERS 'BHP'
                    				
   *COLUMN-FOR  *WELLS 'P-4'
                *PARAMETERS 'Liquid Rate RC'
 
   *COLUMN-FOR  *WELLS 'P-4'
                *PARAMETERS 'Oil Rate SC'   				
  
   *COLUMN-FOR  *WELLS 'P-4'
                *PARAMETERS 'Water Rate RC'            

   *COLUMN-FOR  *WELLS 'P-5'
                *PARAMETERS 'BHP'
                    				
   *COLUMN-FOR  *WELLS 'P-5'
                *PARAMETERS 'Liquid Rate RC'
 
   *COLUMN-FOR  *WELLS 'P-5'
                *PARAMETERS 'Oil Rate SC'   				
  
   *COLUMN-FOR  *WELLS 'P-5'
                *PARAMETERS 'Water Rate RC'  

   *COLUMN-FOR  *WELLS 'P-6'
                *PARAMETERS 'BHP'
                    				
   *COLUMN-FOR  *WELLS 'P-6'
                *PARAMETERS 'Liquid Rate RC'
 
   *COLUMN-FOR  *WELLS 'P-6'
                *PARAMETERS 'Oil Rate SC'   				
  
   *COLUMN-FOR  *WELLS 'P-6'
                *PARAMETERS 'Water Rate RC'  
				
   *COLUMN-FOR  *WELLS 'P-7'
                *PARAMETERS 'BHP'
                    				
   *COLUMN-FOR  *WELLS 'P-7'
                *PARAMETERS 'Liquid Rate RC'
 
   *COLUMN-FOR  *WELLS 'P-7'
                *PARAMETERS 'Oil Rate SC'   				
  
   *COLUMN-FOR  *WELLS 'P-7'
                *PARAMETERS 'Water Rate RC'  

   *COLUMN-FOR  *WELLS 'P-8'
                *PARAMETERS 'BHP'
                    				
   *COLUMN-FOR  *WELLS 'P-8'
                *PARAMETERS 'Liquid Rate RC'
 
   *COLUMN-FOR  *WELLS 'P-8'
                *PARAMETERS 'Oil Rate SC'   				
  
   *COLUMN-FOR  *WELLS 'P-8'
                *PARAMETERS 'Water Rate RC'  
				
   *COLUMN-FOR  *WELLS 'P-9'
                *PARAMETERS 'BHP'
                    				
   *COLUMN-FOR  *WELLS 'P-9'
                *PARAMETERS 'Liquid Rate RC'
 
   *COLUMN-FOR  *WELLS 'P-9'
                *PARAMETERS 'Oil Rate SC'   				
  
   *COLUMN-FOR  *WELLS 'P-9'
                *PARAMETERS 'Water Rate RC'  

   *COLUMN-FOR  *WELLS 'I-1'
     			*PARAMETERS 'BHP'
  
   *COLUMN-FOR  *WELLS 'I-1'
     			*PARAMETERS 'Gas Rate SC'
      
   *COLUMN-FOR  *WELLS 'I-2'
  			    *PARAMETERS 'BHP'

   *COLUMN-FOR  *WELLS 'I-2'
     			*PARAMETERS 'Gas Rate SC'
  	 			
   *COLUMN-FOR  *WELLS 'I-3'
  			    *PARAMETERS 'BHP'

   *COLUMN-FOR  *WELLS 'I-3'
     			*PARAMETERS 'Gas Rate SC'
              
   *COLUMN-FOR  *WELLS 'I-4'
   	    	    *PARAMETERS 'BHP'
				
   *COLUMN-FOR  *WELLS 'I-4'
     			*PARAMETERS 'Gas Rate SC'
  				    
   *COLUMN-FOR  *WELLS 'I-5'
                *PARAMETERS 'BHP' 

   *COLUMN-FOR  *WELLS 'I-5'
     			*PARAMETERS 'Water Rate SC'
				
   *COLUMN-FOR  *WELLS 'I-6'
                *PARAMETERS 'BHP' 

   *COLUMN-FOR  *WELLS 'I-6'
     			*PARAMETERS 'Water Rate SC'

   *COLUMN-FOR  *WELLS 'I-7'
                *PARAMETERS 'BHP' 

   *COLUMN-FOR  *WELLS 'I-7'
     			*PARAMETERS 'Water Rate SC'

   *COLUMN-FOR  *WELLS 'I-8'
                *PARAMETERS 'BHP' 

   *COLUMN-FOR  *WELLS 'I-8'
     			*PARAMETERS 'Water Rate SC'				
		   
*TABLE-END

