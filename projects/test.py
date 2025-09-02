from pydub.generators import Sine

tone = Sine(440).to_audio_segment(duration=1000)  # 1 second of 440Hz tone
tone.export("tone.wav", format="wav")

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/play")
def play():
    return send_file("tone.wav", mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)
