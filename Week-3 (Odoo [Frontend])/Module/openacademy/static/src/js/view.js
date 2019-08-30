/*var AbstractAction = require('web.AbstractAction');
var core = require('web.core');

var OnClick = AbstractAction.extend({
	template: 'simple_html'
})

core.action_registry.add('Tag', OnClick);
xmlDependencies: ['/openacademy/static/src/xml/view_js.xml'],
*/
odoo.define('openacademy.view', function (require) {
    "use strict";

	var AbstractAction = require('web.AbstractAction');
/*	var Widget = require('web.Widget');*/
	var core = require('web.core');

	var  AbstractAction =  AbstractAction.extend({
		template: 'simple_html',
		xmlDependencies: ['/openacademy/static/src/xml/view_js.xml'],

	})

	core.action_registry.add('store',  AbstractAction);

/*    return A;*/
});
