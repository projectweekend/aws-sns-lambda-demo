import io
import os
from zipfile import ZipFile
from boto3.session import Session
from fabric.api import env, task


AWS_ACCESS_KEY_ID = env.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = env.AWS_SECRET_ACCESS_KEY
AWS_REGION = env.get('AWS_REGION', 'us-east-1')


session = Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION)


def can_zip(root, filename):
    excluded_extensions = ['.pyc']
    _, extension = os.path.splitext(filename)
    if extension in excluded_extensions:
        return False


def files_to_zip(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            if can_zip(root=root, filename=f):
                full_path = os.path.join(root, f)
                archive_name = full_path[len(path) + len(os.sep):]
                yield full_path, archive_name


def make_zip_file_bytes(path):
    buf = io.BytesIO()
    with ZipFile(buf, 'w') as z:
        for full_path, archive_name in files_to_zip(path=path):
            z.write(full_path, archive_name)
    return buf.getvalue()


@task
def deploy_lambda(lambda_name):
    lambda_dir = os.path.join('./lambdas', lambda_name)
    if not os.path.isdir(lambda_dir):
        raise ValueError('Lambda directory does not exist: {0}'.format(lambda_dir))
    aws_lambda = session.client('lambda')
    aws_lambda.update_function_code(
        FunctionName=lambda_name,
        ZipFile=make_zip_file_bytes(path=lambda_dir))
