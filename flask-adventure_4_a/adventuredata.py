data = {
    "start": {
        "text": "You are at a junction in the road, you have two choices, which way do you want to go?",
        "image": "path.jpg",

        "audio": "dance.mp3",

        "choices" : {
            "left" : "hole",
            "right" : "wonderland",
            "straight" : "long_way",

        }
    },
    "hole": {
        "text": "You fell down a hole and knocked yourself out!",
        "image": "hole.jpg",
        "choices" : {
            "next" : "end"
        }
    },
    "wonderland": {
        "text": "You have found the paradise of wonderland, congratulations!",
        "image": "wonder_land_2.gif",
        "choices" : {
            "next" : "end"
        }
    },
    "long_way": {
        "text": "You should go go go a long way to the end!",
        "image": "long_way.jpg",
        "choices" : {
            "next" : "end",
            "choose again": "start"
        }




    },
    "end": {
        "text": "Your adventure is over :(",
        "choices" : {
            "Try again" : "start"
        }
    }
}