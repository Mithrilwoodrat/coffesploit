# -*- coding: utf-8 -*-
import os
from server import csfserver
from flask import render_template, flash, jsonify, request, redirect
from config import UPLOAD_FOLDER, allowed_file
from werkzeug.utils import secure_filename
from server import main


@csfserver.route('/')
@csfserver.route('/index')
def index():
    return render_template("index.html")


@csfserver.route('/new_scan')
def new_scan():
    return render_template("new_scan.html")


@csfserver.route('/about')
def about():
    return render_template("about.html", version=main.version())


#@csfserver.route('/setting')
#def setting():
#    return render_template('setting.html', title="Upload your plugin")


@csfserver.route('/upload/<plugin_type>', methods=['POST', 'GET'])
def upload(plugin_type):
    if request.method == "POST":
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, plugin_type+'/'+filename))
    return render_template('setting.html',
                           title=plugin_type+" plugin upload",
                           plugin_type=plugin_type)


@csfserver.route('/set_plugin', methods=['GET'])
def set_plugin():
    plugin_name = request.args.get('plugin', 0, type=str)
    main.use(plugin_name)
    return jsonify(plugin=plugin_name)


@csfserver.route('/plugin/<plugin_name>', methods=['GET', 'POST'])
def plugin(plugin_name):
    if request.method == 'GET':
        main.use(plugin_name)
        plugin_name = main.current_plugin_name()
        plugin_type = main.current_plugin_type()
        print "Using Plugin:", plugin_name
        status = None
        if main.pluginmanager.current_plugin is not None:
            status = main.pluginmanager.plugin_status()
        if status is None:
            return jsonify("ERROR!")
        return jsonify(title=plugin_type+"/"+plugin_name,plugin_name=plugin_name,status=status)

    #if request.method == 'POST':
    #    status = None
    #    if main.pluginmanager.current_plugin is not None:
    #        status = main.pluginmanager.plugin_status()
    #    if status is None:
    #        return jsonify("ERROR!")
    #    for arg in status:
    #        print arg, ":", request.form.get(arg)
    #        plu_arg = request.form.get(arg)
    #        plu_arg = str(plu_arg)
    #        if plu_arg is not None and plu_arg != "":
    #            main.set(str(arg), plu_arg)
    #    return jsonify(status='SUCCESS')


@csfserver.route('/run_plugin', methods=['GET','POST'])
def run_plugin():
    status = main.pluginmanager.plugin_status()
    if request.method == 'POST':
        for arg in status:
            print arg, ":", request.form.get(arg)
            plu_arg = request.form.get(arg)
            plu_arg = str(plu_arg)
            if plu_arg is not None and plu_arg != "":
                main.set(str(arg), plu_arg)
        main.pluginmanager.plugin_run()
        return jsonify(status='SUCCESS')


@csfserver.route('/reports')
def reports():
    if main.pluginmanager.current_plugin_name is None:
        redirect('/index')
    else:
        flash("Plugin is runing please wait!!!!")
        print main.pluginmanager.plugin_result()
    return render_template('reports.html',
                           title=main.current_plugin_name(),
                           result=main.pluginmanager.plugin_result(),
                           )


@csfserver.route('/plugin_list')
def plugin_list():
    plugin_list = main.plugin_list
    scan_plugins = []
    exploit_plugins = []
    payload_plugins = []
    for plugin in plugin_list:
        if plugin_list[plugin][0] == "scan":  # type == scan
            scan_plugins.append(plugin)
        elif plugin_list[plugin][0] == "exploit":  # type == exploit
            exploit_plugins.append(plugin)
        elif plugin_list[plugin][0] == "payload":  # type == payload
            payload_plugins.append(plugin)
    return jsonify({'scan' : scan_plugins,'exploit' : exploit_plugins,'payload': payload_plugins})