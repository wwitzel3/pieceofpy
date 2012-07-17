from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project':'json_serialize_demo'}

@view_config(route_name="custom_object", renderer="json")
def custom_object(request):
    from objects import CustomObject
    results = dict(
        count=2,
        objects=[
            CustomObject('Wayne Witzel III', 'wayne@pieceofpy.com'),
            CustomObject('Fake Person', 'fake.person@pieceofpy.com'),
            ],
        )

    return results

@view_config(route_name="third_party", renderer="json_third_party")
def third_party(request):
    from objects import ThirdPartyObject
    results = dict(
        count=1,
        objects=[
            ThirdPartyObject(),
            ],
        )
    return results

