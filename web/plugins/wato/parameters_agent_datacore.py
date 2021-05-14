#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

import cmk.gui.watolib as watolib
from cmk.gui.plugins.wato import rulespec_registry, HostRulespec
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms, _valuespec_datasource_programs

def _factory_default_special_agents_datacore():
    # No default, do not use setting if no rule matches
    return watolib.Rulespec.FACTORY_DEFAULT_UNUSED

def _valuespec_special_agents_datacore():
    return Dictionary(
        title=_("Check state of DataCore"),
        help=_("This rule selects the DataCore agent, which uses the REST-Api to gather information "
               "about servers, pools, ports and more."),
        elements=[
            ('username',
                TextAscii(
                    title = _('Username'),
                    allow_empty = False
                ),
            ),
            ('password',
                Password(
                    title = _('Password'),
                    allow_empty = False
                ),
            ),
            ('server',
                TextAscii(
                    title = _('Servername to use'),
                    allow_empty = False
                ),
            ),
            ('protocol',
                Alternative(
                    title = _('Protocol'),
                    style = 'dropdown',
                    elements = [
                        FixedValue(
                                0,
                                totext = '',
                                title = _('HTTP'),
                        ),
                        FixedValue(
                                1,
                                totext = '',
                                title = _('HTTPS'),
                        )
                    ]),
            ),
            ('port',
                Integer(
                    title = _('Port'),
                    default_value = 80
                ),
            ),
            ('ssl', FixedValue(
                    0,
                    totext = 'Agent will ignore SSL errors',
                    title = _('Ignore SSL errors'),
                )
            ),
        ],
        optional_keys=['server', 'protocol', 'port', 'ssl'],
    )

rulespec_registry.register(
    HostRulespec(
        factory_default=_factory_default_special_agents_datacore(),
        group=RulespecGroupDatasourcePrograms,
        name="special_agents:datacore",
        valuespec=_valuespec_special_agents_datacore,
    ))
