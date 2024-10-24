from django.shortcuts import render
from django.http import HttpResponse

# Lista de filmes
movies = [
    
    {
        'id': 1,
        'title': 'Suzume no Tojimari',
        'poster': 'img/Suzume.jpg',
        'synopsis': 'Suzume, uma jovem de 17 anos, embarca em uma jornada para fechar misteriosas portas que estão causando desastres por todo o Japão. Durante sua viagem, ela encontra um jovem que a ajuda a entender a magnitude de sua missão e o impacto que essas portas têm no equilíbrio do mundo.',
        'cast': ['Nanoka Hara', 'Hokuto Matsumura', 'Eri Fukatsu']
    },

    
     {
        'id': 2,
        'title': 'Your Name',
        'poster': 'img/YourName.jpg',
        'synopsis': 'Mitsuha, uma jovem do interior, e Taki, um estudante de Tóquio, começam a trocar de corpo misteriosamente. Enquanto vivem a vida um do outro, eles desenvolvem uma conexão especial que os leva a tentar encontrar-se, apesar do tempo e da distância. O filme explora temas de destino, tempo e amor.',
        'cast': ['Ryunosuke Kamiki', 'Mone Kamishiraishi', 'Masami Nagasawa']
    
    },

    
]

def home(request):
    return render(request, 'home.html', {'movies': movies})

def movie_detail(request, id):
    
    movie = next((movie for movie in movies if movie['id'] == id), None)
    
    if movie is None:
        return HttpResponse("Filme não encontrado", status=404)

    return render(request, 'movie_detail.html', {'movie': movie})
