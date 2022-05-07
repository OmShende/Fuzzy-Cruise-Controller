# importing Flask and other modules
from flask import Flask, request, render_template
from scoa_mp2_41261 import CruiseController

# Flask constructor
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        speed_diff = request.form.get("speed_diff")
        acc = request.form.get("acc")
        controller = CruiseController()
        speed_diff = int(speed_diff)
        acc = int(acc)
        throttle = controller.get_throttle(speed_diff, acc)
        throttleStr = "Throttle:" + str(throttle)
        return render_template("result.html", throttleStr=throttleStr)
    return render_template("form.html")


if __name__ == '__main__':
    app.run()
