"""CLI Entrypoint for configuration
"""
import os
import click
from . import sonarr_putio

@click.group()
def cli():
    click.echo('Starting put.io sonarr custom script...')

@cli.command()
@click.option(
    '--putio-folder', default=0, prompt=True,
    help='Folder ID to upload to on put.io',
)
@click.option(
    '--black-hole-folder', default=os.getcwd(),
    type=click.Path(exists=True), prompt=True,
    help='Path to the black hole folder where sonarr puts the torrent/magnet files',
)
@click.option(
    '--watch-folder', default=os.getcwd(),
    prompt=True, type=click.Path(exists=True),
    help='Path to where the files get downloaded from put.io',
)
@click.option(
    '--token', prompt=True, hide_input=True,
    help='put.io OAUTH Token -- see readme for creating your own application',
)
def setup(putio_folder, black_hole_folder, watch_folder, token):
    """Take configuration options and write to settings.txt

    Args:
        putio_folder (int): Folder ID to upload to on put.io
        black_hole_folder (str): Path to the black hole folder where sonarr puts the
            torrent/magnet files
        watch_folder (str): Path to where the files get downloaded from put.io
        token (str): put.io OAUTH Token -- see readme for creating your own application
    """
    click.echo('Saving settings to %s' % click.get_app_dir('sonarr_putio'))

    config_file = click.get_app_dir('sonarr_putio')
    if not os.path.isdir(os.path.dirname(config_file)):
        os.makedirs(os.path.dirname(config_file))
    settings = open(config_file, 'w')
    settings.write(black_hole_folder + '\n')
    settings.write(watch_folder + '\n')
    settings.write(token + '\n')
    settings.write(str(putio_folder) + '\n')
    settings.close()

@cli.command()
def upload():
    """Uploads Magnet Files from Sonnar to Put.io
    """
    click.echo('Uploading files to put.io')
    sonarr_putio.upload()


@cli.command()
def download():
    """Downloads files from put.io to the watch folder
    """
    click.echo('Downloading files from put.io')
    sonarr_putio.download()


if __name__ == '__main__':
    setup()
