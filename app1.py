from flask import Flask,request,jsonify

app = Flask(__name__)

Movies= [
    {"id":101,"Name":"Dhuradar" ,"Category":"action"} ,
    {"id":102,"Name":"Mirror" ,"Category":"action"},
    {"id":103,"Name":"Cocktail" ,"Category":"romantic"},
    {"id":104,"Name":"Saiyara" ,"Category":"romantic"},
    {"id":105,"Name":"Mirazapur" ,"Category":"action"}

]

@app.route("/Movies",methods=['GET'])
def get_Movie():
    return jsonify(Movies)


@app.route("/Movies",methods=['POST'])
def Movie():

    data=request.get_json()

    Movies.append(data)

    return jsonify(
        {
           "msg":"Movies data added successfully" ,
           "Movies":data
        }
    )

app.run(debug=True)