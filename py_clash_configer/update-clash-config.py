from io import StringIO
from pathlib import Path

import click

import requests
import yaml


def download(url: str):
    print('download from:', url)
    with requests.get(url) as resp:
        assert resp.ok
        assert 'yaml' in resp.headers['content-type'].lower()
        return resp.text


def patch_yaml(f1, f2):
    y1 = yaml.safe_load(f1)
    y2 = yaml.safe_load(f2)
    # TODO replace shallow merge with rule-based merge
    y1.update(y2)
    return yaml.safe_dump(y1, encoding='utf-8')


def update(url, patch, out):
    config = download(url)
    if patch:
        subscription = StringIO(config)
        print('patch with', patch)
        with open(patch) as local, open(out, 'wb') as outf:
            print('save to', out)
            outf.write(patch_yaml(subscription, local))
    else:
        with open(out, 'w', encoding='utf-8') as outf:
            print('save to', out)
            outf.write(config)


@click.command()
@click.option(
    '--local', '-l',
    nargs=1,
    help='patch donwloaded configuration with content in specified file',
)
@click.option(
    '--output-dir', '-o',
    nargs=1,
    help='directory for final config.yaml file, default: ~/.config/clash',
    default='~/.config/clash',
)
@click.argument('url')
@click.help_option('-h')
def main(url, local, output_dir):
    out = Path(output_dir, 'config.yaml').expanduser()
    if local:
        local = Path(local).expanduser()
    print(local)
    print(out)
    update(url, local, out)


if __name__ == '__main__':
    main()
