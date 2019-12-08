from flask import Blueprint, render_template

bp = Blueprint("public", __name__)


@bp.route("/")
def home():
    return render_template("public/home/index.html")


@bp.route("/blog")
def blog():
    blogs = [
        {
            "author": "Paulo Sairel Don",
            "date": "2019-01-01",
            "title": "First Blog",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rutrum, enim vel condimentum rhoncus, est eros sollicitudin justo, at semper nisi nisl id urna. Aenean tincidunt hendrerit sollicitudin. Etiam ac convallis tortor. Aliquam tempus nunc eget lacus tristique facilisis. Cras non nulla suscipit, aliquet felis vitae, cursus risus. Nulla facilisi. Integer ante arcu, egestas a tellus id, egestas ullamcorper turpis. Maecenas libero augue, posuere et tellus ut, rutrum tincidunt leo. Cras mollis lectus et quam tempus, ac ullamcorper lacus lacinia. Quisque porttitor arcu ut ante aliquam, id sodales arcu varius. Vivamus ullamcorper dolor quis dui euismod sollicitudin. Donec molestie dolor ut arcu congue sollicitudin. Integer nec elit euismod, viverra turpis eu, sodales elit. Etiam a eros et sem semper pulvinar vitae a enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
            "author": "Paulo Sairel Don",
            "date": "2019-01-02",
            "title": "2nd Blog",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rutrum, enim vel condimentum rhoncus, est eros sollicitudin justo, at semper nisi nisl id urna. Aenean tincidunt hendrerit sollicitudin. Etiam ac convallis tortor. Aliquam tempus nunc eget lacus tristique facilisis. Cras non nulla suscipit, aliquet felis vitae, cursus risus. Nulla facilisi. Integer ante arcu, egestas a tellus id, egestas ullamcorper turpis. Maecenas libero augue, posuere et tellus ut, rutrum tincidunt leo. Cras mollis lectus et quam tempus, ac ullamcorper lacus lacinia. Quisque porttitor arcu ut ante aliquam, id sodales arcu varius. Vivamus ullamcorper dolor quis dui euismod sollicitudin. Donec molestie dolor ut arcu congue sollicitudin. Integer nec elit euismod, viverra turpis eu, sodales elit. Etiam a eros et sem semper pulvinar vitae a enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
        {
            "author": "Juan Dela Cruz",
            "date": "2019-01-02",
            "title": "Something Interesting",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rutrum, enim vel condimentum rhoncus, est eros sollicitudin justo, at semper nisi nisl id urna. Aenean tincidunt hendrerit sollicitudin. Etiam ac convallis tortor. Aliquam tempus nunc eget lacus tristique facilisis. Cras non nulla suscipit, aliquet felis vitae, cursus risus. Nulla facilisi. Integer ante arcu, egestas a tellus id, egestas ullamcorper turpis. Maecenas libero augue, posuere et tellus ut, rutrum tincidunt leo. Cras mollis lectus et quam tempus, ac ullamcorper lacus lacinia. Quisque porttitor arcu ut ante aliquam, id sodales arcu varius. Vivamus ullamcorper dolor quis dui euismod sollicitudin. Donec molestie dolor ut arcu congue sollicitudin. Integer nec elit euismod, viverra turpis eu, sodales elit. Etiam a eros et sem semper pulvinar vitae a enim. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
    ]
    return render_template("public/blog/index.html", blogs=blogs)
