# https://docs.python.org/3/library/exceptions.html

# Error handling

# Custom exception
class CannotBeZeroException(Exception):
    """
    Exception raise when for errors if age 0

    Attributes:
        age -- input age
        message -- the message
    """
    def __init__(self, age, message="Cannot be zero") -> None:
        self.age = age
        self.message = message
        super().__init__(self.message)

while True:
    try:
        age = int(input('What is your age ? '))
        10/age
        # if age is 0:
        #     raise CannotBeZeroException(age)

        #raise ValueError('Stop it')

        print(age)
    #except (ValueError, ZeroDivisionError) as err: # we can handle two exceptions at one
    #    print(f'Oppsss something is not right, err: {err}')
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError as err:
        print(f'An error occured during process, error details: {err}')
    else:
        print('Thank you')
        break
    finally:
        print('ok, I am finally done')