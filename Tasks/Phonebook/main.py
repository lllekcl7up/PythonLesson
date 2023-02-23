from controller import get_operation_number,perform_operation
import user_interface as ui

operation = '1'
while (operation != '0'):
    ui.console_menu()
    operation = get_operation_number()
    perform_operation(operation)

