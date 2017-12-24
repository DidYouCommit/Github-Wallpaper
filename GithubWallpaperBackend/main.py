from flask import Flask, request, jsonify
# from flask import send_file

from parse import get_grass_field

app = Flask(__name__)


@app.route('/image', methods=['GET'])
def image():
    username = request.args['username']

    field = get_grass_field(username)
    if field:
        return jsonify(field), 200
    else:
        return '', 204

#    im = get_grass_field(username)

#    if im:
#        return send_file(username+'.jpg', as_attachment=True, attachment_filename='grass_field.jpg'), 200
#    else:
#        return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1024)