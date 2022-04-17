#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from typing import Type, Optional, List
from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Alternative,
    Dictionary,
    Integer,
    Tuple,
    FixedValue,
    TextAscii,
)
from cmk.gui.plugins.wato import (
    RulespecGroupCheckParametersApplications,
    CheckParameterRulespecWithItem,
    rulespec_registry,
)


def _parameter_valuespec_datacore_server():
    return Dictionary(
        title = _('Parameter'),
        optional_keys = ['serverstate'],
        elements = [
            ( 'serverstate', Dictionary(
                title = _('Server Status'),
                optional_keys = ['0', '1', '2', '3'],
                elements = [
                    ( '0', Alternative(
                        title = _('Not Present'),
                        style = 'dropdown',
                        elements = [
                            FixedValue(
                                    0,
                                    totext = 'show as OK',
                                    title = _('show as OK'),
                            ),
                            FixedValue(
                                    1,
                                    totext = 'show as WARN',
                                    title = _('show as WARN'),
                            ),
                            FixedValue(
                                    2,
                                    totext = 'show as CRIT',
                                    title = _('show as CRIT'),
                            ),
                        ])
                    ),
                    ( '1', Alternative(
                        title = _('Offline'),
                        style = 'dropdown',
                        elements = [
                            FixedValue(
                                    0,
                                    totext = 'show as OK',
                                    title = _('show as OK'),
                            ),
                            FixedValue(
                                    1,
                                    totext = 'show as WARN',
                                    title = _('show as WARN'),
                            ),
                            FixedValue(
                                    2,
                                    totext = 'show as CRIT',
                                    title = _('show as CRIT'),
                            ),
                        ])
                    ),
                    ( '2', Alternative(
                        title = _('Online'),
                        style = 'dropdown',
                        elements = [
                            FixedValue(
                                    0,
                                    totext = 'show as OK',
                                    title = _('show as OK'),
                            ),
                            FixedValue(
                                    1,
                                    totext = 'show as WARN',
                                    title = _('show as WARN'),
                            ),
                            FixedValue(
                                    2,
                                    totext = 'show as CRIT',
                                    title = _('show as CRIT'),
                            ),
                        ])
                    ),
                    ( '3', Alternative(
                        title = _('Failed'),
                        style = 'dropdown',
                        elements = [
                            FixedValue(
                                    0,
                                    totext = 'show as OK',
                                    title = _('show as OK'),
                            ),
                            FixedValue(
                                    1,
                                    totext = 'show as WARN',
                                    title = _('show as WARN'),
                            ),
                            FixedValue(
                                    2,
                                    totext = 'show as CRIT',
                                    title = _('show as CRIT'),
                            ),
                        ])
                    )
                ])
            ),

        ]
    )

def _item_spec_datacore_server():
    return TextAscii(title=_("Device-ID"))

rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name="datacore_server",
        group=RulespecGroupCheckParametersApplications,
        item_spec=_item_spec_datacore_server,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_datacore_server,
        title=lambda: _('Checksettings for DataCore Server')
    )
)
