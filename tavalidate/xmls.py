from io import BytesIO

from lxml import etree
from typing import Mapping

from box import Box

from tavalidate.log import logger


def do_save_xml(resp, **kwargs):
    """
    Extract data from response xml body

    :param resp:
    :param kwargs.variables: variable name -> xpath mapping.
    :return:
    """
    source_xml = resp.text
    logger.debug("Response body: {}".format(source_xml))
    variables: Mapping = kwargs['variables']
    source_et = etree.parse(BytesIO(bytes(source_xml, "UTF-8")))
    assert source_et is not None, "Can not parse response body"

    data = dict()
    for var in variables.items():
        it = _extract(source_et, var[1])
        assert it is not None, "Can not read {} from response".format(var[1])
        data[var[0]] = it
        logger.debug("{} => {}".format(var[0], it))

    return Box(data)


def _extract(root, xp):
    ar = root.xpath(xp)
    if len(ar) <= 0:
        return None
    if len(ar) > 1:
        logger.info("XPath {} produces more than 1 results, the first is used."
                    .format(xp))
    return ar[0]


save_xml = do_save_xml
