

def get_number_input(prompt):

    '''
use prompt to collect input and return float
    '''


    # initialize value
    value = None
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value
        
        except ValueError as e:
            print("Invalid Input")
            print(e, file=ERROR_FILE)


def main():
    while True:
        client_name = input("What is the customer\'s name?: ")
        if not client_name:
            break


        while True:
            product_name= input("What is the product name? ")
            if not product_name:
                break


            Product_qty = get_number_input(f'How many {product_name} purchased?: ')
            product_price = get_number_input(f'How much is the price of the {product_name}?: ')

if __name__ == '__main__':

    #Super global
    ERROR_FILE = open('error_log.txt', 'a')

    #the main code
    main()

    #close file
    ERROR_FILE.close()

            
            
            
