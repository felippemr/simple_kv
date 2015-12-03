from put import handle_put
from get import handle_get
from get_list import handle_getlist
from put_list import handle_putlist
from increment import handle_increment
from append import handle_append
from delete import handle_delete
from stats import handle_stats
from update_stats import update_stats

COMMAND_HANDLERS = {
    'PUT': handle_put,
    'GET': handle_get,
    'GETLIST': handle_getlist,
    'PUTLIST': handle_putlist,
    'INCREMENT': handle_increment,
    'APPEND': handle_append,
    'DELETE': handle_delete,
    'STATS': handle_stats,
    'UPDATE_STATS': update_stats,
}
