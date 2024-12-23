import toml
from loguru import logger
def get_setting(file_path):
    """
    Reads the toml file and returns the setting
    """
    try:
        settings = toml.load(file_path)
        return settings
    except Exception as e:
        logger.error(e)


def get_env(file_path):
    try:
        settings = get_setting(file_path)
        project = settings['project']
        git_ip = settings['codeAddress']['ip']
        git_module = settings['codeAddress']['moduleName']
        master_branch = settings['codeAddress']['masterBranch']
        temp_branch = settings['codeAddress']['tempBranch']
        git_long_path = settings['codeAddress']['longPathsCode']
        maven_version = settings['toolsConfig']['mavenVersion']
        return project, git_ip, git_module, master_branch, temp_branch, git_long_path, maven_version
    except Exception as e:
        logger.error(e)