from config import demo_api_key
from next_bus import get_next_bus

def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return launch_request_handler(request)

@alexa.intent(intent="AMAZON.HelpIntent")
def help_intent_handler(request):
    msg = ("I want to help your travel plans! "
           "Right now, I can only tell you the number of minutes until the next 70 bus outside of the apartment that's heading south")
    return r.create_response(message=msg)

@alexa.intent(intent="AMAZON.StopIntent")
def stop_intent__handler(request):
    return cancel_action_handler(request)

@alexa.intent(intent="NextBusTime")
def list_bus_times(request):
    return get_next_bus()
