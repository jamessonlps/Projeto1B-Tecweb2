from django.shortcuts import get_object_or_404, render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = None

        all_tags = Tag.objects.all()

        # Verifica se uma tag foi inserida
        if request.POST.__contains__('tag'):
            tag_input = request.POST.get('tag')
            # verifica se a tag não está vazia
            if tag_input.replace(" ", "") != "":
                tag = Tag(text=tag_input)
                # verifica se a tag já existe
                for tag_db in all_tags:
                    if tag_db.text == tag_input:
                        tag = tag_db
                        break

        new_note = Note(title=title, content=content, tag=tag)

        # request para criar nota
        if request.POST.__contains__('create'):
            if tag is not None:
                tag.save()
            new_note.save()
        
        # Verifica se contém id (para solicitações de delete)
        if request.POST.__contains__('id'):
            note_id = request.POST.get('id')
            note = Note(id=note_id, content=content, tag=tag)

        # request para deletar note
        if request.POST.__contains__('delete'):
            note.delete()

        return redirect('/')
    else:
        all_notes = Note.objects.all()
        return render(
            request=request, 
            template_name='notes/index.html', 
            context={ 'notes': all_notes }
        )


def tags(request):
    all_tags = Tag.objects.all()
    count = {}
    for tag in all_tags:
        count[tag.id] = Note.objects.filter(tag__id__exact=tag.id).count() or 0

    context = { 
        "tags": all_tags, 
        "counter": count
    }
    
    return render(
        request=request,
        template_name='notes/tags.html',
        context=context
    )



def note_view(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    tag_entry = note.tag

    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = tag_entry

        all_tags = Tag.objects.all()

        # Verifica se uma tag foi inserida
        if request.POST.__contains__('tag'):
            tag_input = request.POST.get('tag')
            # verifica se a tag não está vazia
            if tag_input.replace(" ", "") != "":
                tag = Tag(text=tag_input)
                # verifica se a tag já existe
                for tag_db in all_tags:
                    if tag_db.text == tag_input:
                        tag = tag_db
                        break

        note_updated = Note(id=note_id, title=title, content=content, tag=tag)

        # request para atualizar nota
        if request.POST.__contains__('update'):
            if ((tag is not None) and (tag not in all_tags)):
                tag.save()
            note.delete()
            note_updated.save()

        return redirect('/')

    else:
        return render(
            request=request,
            template_name='notes/note_view.html',
            context={ "note": note }
        )


def notes_by_tag(request, tag_id):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = get_object_or_404(Tag, pk=tag_id)

        all_tags = Tag.objects.filter(id__exact=tag_id)

        # Verifica se uma tag foi inserida
        if request.POST.__contains__('tag'):
            tag_input = request.POST.get('tag')
            # verifica se a tag não está vazia
            if tag_input.replace(" ", "") != "":
                tag = Tag(text=tag_input)
                # verifica se a tag já existe
                for tag_db in all_tags:
                    if tag_db.text == tag_input:
                        tag = tag_db
                        break

        new_note = Note(title=title, content=content, tag=tag)

        # request para criar nota
        if request.POST.__contains__('create'):
            if tag is not None:
                tag.save()
            new_note.save()
        
        # Verifica se contém id (para solicitações de delete)
        if request.POST.__contains__('id'):
            note_id = request.POST.get('id')
            note = Note(id=note_id, content=content, tag=tag)

        # request para deletar note
        if request.POST.__contains__('delete'):
            note.delete()

        return redirect('/')
    else:
        all_notes = Note.objects.all().filter(tag__id__exact=tag_id)
        tag_ = get_object_or_404(Tag, pk=tag_id)
        return render(
            request=request, 
            template_name='notes/notes_by_tag.html', 
            context={
                'notes': all_notes,
                'tag': tag_
            }
        )