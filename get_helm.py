import json
import os
import stat
import sys
import tarfile
import tempfile
from urllib import request


def github_get_latest_release(owner, repo):
    uri = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    response = request.urlopen(uri)
    return json.loads(response.read())


def download_file_to_path(source, dest):
    response = request.urlopen(source)
    with open(dest, 'wb') as f:
        f.write(response.read())


def make_file_executable(file_path):
    st = os.stat(file_path)
    os.chmod(file_path, st.st_mode | stat.S_IEXEC)


def extract_file(archive, source, destination):
    with tarfile.open(archive, 'r:gz') as tf:
        with open(destination, 'wb') as f:
            f.write(tf.extractfile(source).read())


if __name__ == '__main__':
    assert len(sys.argv) == 2, 'Usage: python get_helm.py /path/to/dest'
    latest_release = github_get_latest_release(
        'kubernetes', 'helm')['tag_name']
    print(f'Latest version is {latest_release!r}')
    helm_dest = sys.argv[1]

    with tempfile.TemporaryDirectory() as temp_dir:
        tgz_file = f'{temp_dir}/helm.tar.gz'
        download_file_to_path(
            'https://storage.googleapis.com/kubernetes-helm/'
            f'helm-{latest_release}-linux-amd64.tar.gz',
            tgz_file
        )
        extract_file(tgz_file, 'linux-amd64/helm', helm_dest)

    make_file_executable(helm_dest)
    print(f'Downloaded to {helm_dest!r}')
