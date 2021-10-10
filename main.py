import docker


class AWSECSBackend:
    """ Design a class that will run docker containers and run commands from them. """
    def __init__(self, image):
        self.container = docker.from_env()
        self.image = image

    def run_command(self, cmd):
        return self.container.containers.run(self.image,cmd)



class DockerLocalBackend:
    """ Design a class that will run docker containers and run commands from them. """
    def __init__(self, image):
        self.container = docker.from_env()
        self.image = image

    def run_command(self, cmd):
        return self.container.containers.run(self.image,cmd)


class PackerBuild(DockerLocalBackend):
    def __init__(self, image, github_url):
        super().__init__(image)
        self.github_url = github_url
    
    def run_build(self):
        pass

class TerraformBuild(DockerLocalBackend):
    def __init__(self, image, github_url):
        super().__init__(image)
        self.github_url = github_url
    
    def run_build(self):
        pass


import argparse
parser = argparse.ArgumentParser(description="Terraform Automation Tool")
parser.add_argument('--cmd', help='command to run in container')
args = vars(parser.parse_args())

def entrypoint():
    """
    Command application that will 
    """
    #print(args['cmd'])
    command= args['cmd'] 
    worker = DockerLocalBackend('teraconductor:latest')
    print(worker.run_command(command))
    

    # print(comment)

    # Single line comment
     



if __name__ == '__main__':
    entrypoint()
