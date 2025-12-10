is_simple_core = False  # True

if is_simple_core:
    from Pedro_package.core_simple import Pedro_Variable
    from Pedro_package.core_simple import Pedro_Function
    from Pedro_package.core_simple import using_config
    from Pedro_package.core_simple import no_grad
    from Pedro_package.core_simple import as_array
    from Pedro_package.core_simple import as_variable
    from Pedro_package.core_simple import setup_variable
else:
    from Pedro_package.core import Pedro_Variable
    from Pedro_package.core import Pedro_Function
    from Pedro_package.core import using_config
    from Pedro_package.core import no_grad
    from Pedro_package.core import as_array
    from Pedro_package.core import as_variable
    from Pedro_package.core import setup_variable
    from Pedro_package.core import Pedro_Parameter
    from Pedro_package.layer import Pedro_Layer
    from Pedro_package.models import Pedro_Model


setup_variable()