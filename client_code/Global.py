import anvil.server
import anvil.users

global_dict = {
    'user': None
}

def __getattr__(name):
    if name in global_dict:
        if name == 'user':
            global_dict[name] = global_dict[name] or anvil.users.get_user()
        else:
            global_dict[name] = global_dict[name] or anvil.server.call('get_' + name)
        return global_dict[name]
    raise AttributeError(name)