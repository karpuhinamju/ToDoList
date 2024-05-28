from datetime import datetime, timedelta
import pickle
def timedelta_str(delta: timedelta):
    s = ""
    if delta.days != 0:
        s += f"{delta.days} days "

    hours = delta.seconds // 3600
    minutes = (delta.seconds - 3600 * hours) // 60
    s += f"{hours}h {minutes}m"
    return s



def save_to_file(filename: str, object):
    with open(filename, 'wb') as f:
        pickle.dump(object, f, protocol=pickle.HIGHEST_PROTOCOL)