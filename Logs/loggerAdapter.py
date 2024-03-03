import logging

class CustomAdapter(logging.LoggerAdapter):
    #  self là một tham chiếu đến thể hiện hiện tại của lớp
    # tườn tự this
    def process(self, msg, kwargs):
        # use my_context from kwargs or the default given on instantiation
        my_context = kwargs.pop('my_context', self.extra['my_context'])
        return '[%s] %s' % (my_context, msg), kwargs

logger = logging.getLogger(__name__)
syslog = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
syslog.setFormatter(formatter)
logger.addHandler(syslog)

adapter = CustomAdapter(logger, {'my_context': '6666'})
logger.setLevel(logging.INFO)

adapter.info('The cat meowed', my_context='8888')
adapter.info('The cat meowed')