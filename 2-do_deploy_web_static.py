#!/usr/bin/python3
""" a Fabric script (based on the file 1-pack_web_static.py) that distributes..
    ..an archive to your web servers, using the function do_deploy: """


from fabric.api import env, put, run
from os.path import exists


env.hosts = ['100.26.50.2', '35.175.65.7']  # <IP web-01>, <IP web-02>
# ^ All remote commands must be executed on your both web servers
# (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)



def do_deploy(archive_path):
    """
    distributes an archive to my web servers
    """
    if not exists(archive_path):
        return False  # Returns False if the file at archive_path doesn't exist

    try:
        # Get the archive filename without extension
        filename = archive_path.split("/")[-1]
        archive_no_ext = filename.split(".")[0]

        # Remote paths
        remote_tmp = "/tmp/{}".format(filename)
        release_path = "/data/web_static/releases/{}".format(archive_no_ext)
        current_path = "/data/web_static/current"

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, remote_tmp)

        # Uncompress the archive to the release path
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(remote_tmp, release_path))
        run("rm {}".format(remote_tmp))

        # Move contents to the release path and remove old contents
        run("mv {}/web_static/* {}/".format(release_path, release_path))
        run("rm -rf {}/web_static".format(release_path))

        # Remove the current symbolic link
        run("rm -rf {}".format(current_path))

        # Create a new symbolic link to the new version
        run("ln -s {} {}".format(release_path, current_path))
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
