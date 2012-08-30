import json
import cyclone.web
from twisted.application import service, internet

class HttpHandler(cyclone.web.RequestHandler):

    def _load_request_body_as_json(self):
        return json.loads(self.request.body)

    def post(self):
        doc = self._load_request_body_as_json()
        print doc

        doc_is_done = doc.get('done')
        metadata_key = doc.get('metadata_key')
        if doc_is_done:
            doc_status = "done"
        else:
            doc_status = "not done"
        print("Document with uid %s is %s.\n" % (doc.get('doc_key'), doc_status))
        print("Metadata key: %s" % str(metadata_key))

class CallbackService(cyclone.web.Application):

    def __init__(self):
        handlers = [
            (r"/", HttpHandler),
        ]

        settings = {
                'xheaders':True,
                }

        cyclone.web.Application.__init__(self, handlers, **settings)

application = service.Application("Callback Service")
srv = internet.TCPServer(8886, CallbackService(), interface='0.0.0.0')
srv.setServiceParent(application)