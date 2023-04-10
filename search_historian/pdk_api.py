# pylint: disable=line-too-long

import importlib

def compile_report(generator, sources, data_start=None, data_end=None, date_type='created'): # pylint: disable=too-many-locals, too-many-branches, too-many-statements
    try:
        generator_module = importlib.import_module('.generators.' + generator.replace('-', '_'), package='search_historian')

        output_file = None

        try:
            output_file = generator_module.compile_report(generator, sources, data_start=data_start, data_end=data_end, date_type=date_type)
        except TypeError:
            print('TODO: Update ' + generator + '.compile_report to support data_start, data_end, and date_type parameters!')

            output_file = generator_module.compile_report(generator, sources)

        if output_file is not None:
            return output_file
    except ImportError:
        pass
    except AttributeError:
        pass

    return None
