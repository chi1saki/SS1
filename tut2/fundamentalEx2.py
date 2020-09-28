def main()
    months = ['January', 'February,', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    date_input = input('Enter date in the format mm/dd/yyyy: ').split('/')
    month = months[int(date_input[0]) - 1]
    day = int(date_input[1])
    year = int(date_input[2])
    print('The date is {} {}, {}'.format(month, day, year))
main()