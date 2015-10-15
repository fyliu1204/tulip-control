# Copyright (c) 2015 by California Institute of Technology
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the California Institute of Technology nor
#    the names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior
#    written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL CALTECH
# OR THE CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
# USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
"""
Interface to gr1py

U{https://pypi.python.org/pypi/gr1py}
U{https://github.com/slivingston/gr1py}
"""
from __future__ import absolute_import

import logging
logger = logging.getLogger(__name__)
import gr1py
import gr1py.cli
from tulip.spec import GRSpec, translate
from tulip.interfaces.gr1c import load_aut_json


_hl = 60 * '-'


def check_realizable(spec, init_option="ALL_ENV_EXIST_SYS_INIT"):
    """Decide realizability of specification.

    Consult the documentation of L{synthesize} about parameters.

    @return: True if realizable, False if not, or an error occurs.
    """
    s = translate(spec, 'gr1c')
    logger.info('\n{hl}\n gr1py input:\n {s}\n{hl}'.format(s=s, hl=_hl))
    tsys, exprtab = gr1py.cli.loads(s)
    return gr1py.solve.check_realizable(tsys, exprtab)

def synthesize(spec, init_option="ALL_ENV_EXIST_SYS_INIT"):
    """Synthesize strategy realizing the given specification.

    cf. L{tulip.interfaces.gr1c.synthesize}
    """
    s = translate(spec, 'gr1c')
    logger.info('\n{hl}\n gr1py input:\n {s}\n{hl}'.format(s=s, hl=_hl))
    tsys, exprtab = gr1py.cli.loads(s)
    strategy = gr1py.solve.synthesize(tsys, exprtab)
    if strategy is None:
        return None
    else:
        return load_aut_json(gr1py.output.dump_json(tsys.symtab, strategy))