# -*- coding: utf-8 -*-
from server import csfserver
from flask import render_template, flash, jsonify, request, redirect, url_for
from server import main



@csfserver.route('/')
@csfserver.route('/index')
def index():
    return render_template("index.html")


@csfserver.route('/about')
def about():
    return render_template("about.html")


@csfserver.route('/config')
def config():
    plugin_list = main.plugin_list()
    scan_plugins = []
    exploit_plugins = []
    payloads_plugins = []
    for plugin in plugin_list:
        if plugin_list[plugin][0] == "scan":  # type == scan
            scan_plugins.append(plugin)
    flash("Click button to choose plugin")
    return render_template("config.html", title="Choose Plugin",
                           scan_plugins=scan_plugins)


@csfserver.route('/_set_plugin', methods=['GET'])
def set_plugin():
    plugin_name = request.args.get('plugin', 0 , type=str)
    return jsonify(plugin=plugin_name)


@csfserver.route('/plugin/<plugin_name>', methods=['GET', 'POST'])
def plugin(plugin_name=None):
    main.use(plugin_name)
    print "Using Plugin:", main.current_plugin_name()
    status = None
    if main.pluginmanager.current_plugin is not None:
        status = main.pluginmanager.plugin_status()
    if status is None:
        flash("error while parse status")
    else:
        flash("Please set plugin's argments")
    if request.method == 'POST':
        for arg in status:
            print arg, ":", request.form.get(arg)
            plu_arg = request.form.get(arg)
            plu_arg = str(plu_arg)
            if plu_arg is not None and plu_arg != "":
                main.set(str(arg),plu_arg)
        return redirect(url_for('reports'))
    return render_template("plugin.html", title=plugin_name,
                           plugin_name=plugin_name,
                           status=status)


@csfserver.route('/reports')
def reports():
    flash("Plugin is runing please wait!!!!")
    main.pluginmanager.current_plugin.run()
    main.pluginmanager.plugin_result()
    return render_template('reports.html',
                           title=main.current_plugin_name(),
                           result=main.pluginmanager.plugin_result(),
                           )


@csfserver.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@csfserver.route('/test')
def test():
    return render_template('test.html')