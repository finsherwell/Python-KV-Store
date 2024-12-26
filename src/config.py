import os

def determine_persistence_path(name):
    user_home = os.path.expanduser("~")
    persistence_dir = os.path.join(user_home, name)

    if not os.path.exists(persistence_dir):
        os.makedirs(persistence_dir)
    
    return persistence_dir