import logging
import dispatcher
import sys
from speaker import greet_user
from listener import take_user_input

def main():
    """The default method for this module.
    
    Starts monitoring for input from the user, then dispatches the requests based on what was asked.
    
    """
    
    greet_user()
    
    try:
        while True:
            query = take_user_input()
            
            if query is not None:
                query = query.lower()
                dispatcher.dispatch(query)
            else:
                print(f"Query is: {query}")
                
    except (KeyboardInterrupt):
        print('\nGoodbye.')
        sys.exit()
    except Exception as e:
        logging.critical(e)
        sys.exit()

if __name__ == '__main__':
    # Set up logging
    level = logging.WARNING
    format = '[%(levelname)s] %(asctime)s - %(message)s [%(filename)s:%(lineno)s %(funcName)s]'
    logging.basicConfig(level=level, format=format)
    
    main()