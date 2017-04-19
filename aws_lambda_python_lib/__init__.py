import os

__version__ = '0.0.3'

# A manifest of the included packages.
aws_lambda_python_lib = {
    'pdfkit': {
        'version': '0.6.1',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'pdfkit', 'pdfkit-0.6.1.tar.gz')
    }
}
