"""Uploads Magnet Files from Sonnar to Put.io and Downloads TV Shows
"""
import os

import click
import putiopy as putio


def get_settings():
    """Get Settings"""
    with open(click.get_app_dir('sonarr_putio')) as settings:
        lines = settings.read().splitlines()
        return lines


def putio_upload(client, path, parent_id):
    """Upload magnet Link from File
    """
    for t_file in os.listdir(path):
        if t_file.endswith(".magnet"):
            with open(path + t_file, 'r') as magnet:
                for line in magnet:
                    click.echo('Adding %s to %s' % (line, parent_id))
                    client.Transfer.add_url(line, parent_id)
            os.remove(os.path.join(path, t_file))
        elif t_file.endswith('.torrent'):
            click.echo('Adding %s to %s' % (t_file, parent_id))
            client.Transfer.add_torrent(path + t_file, parent_id)
            os.remove(os.path.join(path, t_file))


def putio_download(client, path, folderid):
    """Download from put.io
    """
    transfer_list = client.Transfer.list()
    transferlen = len(transfer_list)
    files = client.File.list(folderid)

    if transferlen != 0:
        os.chdir(path)
        for t_file in files:
            client.File.download(t_file)
            client.File.delete(t_file)
        client.Transfer.clean()


def init():
    """Create a putio client object to use
    """
    settings = get_settings()
    client = putio.Client(settings[2], use_retry=True, timeout=30)
    return settings, client


def upload():
    """Upload the torrent/magnet files in the black hole directory to put.io
    """
    settings, client = init()
    putio_upload(client, settings[0] + '/', settings[3])


def download():
    """Download files from put.io to the watch folder
    """
    settings, client = init()
    putio_download(client, settings[1] + '/', settings[3])
