def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return 'Not a valid number'
    except (ValueError, TypeError) as err:
        return err