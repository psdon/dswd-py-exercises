def create_blog(data=None, db=None, Model=None):
    if not data:
        data = [
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

    for entry in data:
        blog = Model(author=entry['author'], title=entry['title'], content=entry['content'])
        db.session.add(blog)
        try:
            db.session.commit()
        except Exception as err:
            db.session.rollback()
            print("Failure occured")
            print(err)



# from dswd_blog.extensions import db
# from dswd_blog.models import Blog
# from scripts.commit_blog_data import create_blog
# create_blog(db=db, Model=Blog)