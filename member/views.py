import json
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.views import View
from .models import Members
from derby.models import Fight, Entry
from .forms import MemberRegistration
# Create your views here.


class Index(View):
    template_name = 'member/index.html'
    context = {}

    def get(self, request, **kwargs):
        page_num = request.GET.get('page', 1)
        form = MemberRegistration()
        member_list = Members.objects.filter(user_id=request.user.id).order_by('-id')
        paginator = Paginator(member_list, 3)
        total_member = paginator.count
        try:
            members = paginator.page(page_num)
        except PageNotAnInteger:
            members = paginator.page(1)
        except EmptyPage:
            members = paginator.page(1)
        self.context = {'form': form, 'members': members, 'total_member': total_member}
        return render(request, template_name=self.template_name, context=self.context)

    def post(self, request, **kwargs):
        page_num = request.GET.get('page', 1)
        form = MemberRegistration(request.POST)
        member_list = Members.objects.filter(user_id=request.user.id).order_by('-id')
        paginator = Paginator(member_list, 3)        
        try:
            members = paginator.page(page_num)
        except PageNotAnInteger:
            members = paginator.page(1)
        except EmptyPage:
            members = paginator.page(1)

        self.context = {'form': form, 'members': members}
        if form.is_valid():
            member = Members(user_id=request.user.id,
                             owner=form.cleaned_data.get('owner'),
                             farm_name=form.cleaned_data.get('farm_name'),
                             location=form.cleaned_data.get('location'),
                             email=form.cleaned_data.get('email'),
                             contact_number=form.cleaned_data.get('contact_number'))
            member.save()
            form = MemberRegistration()
            self.context['form'] = form
            self.context['success_add_member'] = 'You successfully added a new member.' 
        self.context['total_member'] = paginator.count       
        return render(request, template_name=self.template_name, context=self.context)


class Profile(View):
    template_name = 'member/member_profile.html'
    context = {}

    def get(self, request, **kwargs):
        member_id = kwargs['member_id']
        member = Members.objects.get(id=member_id, user_id=request.user.id)
        fights = Fight.objects.filter(owner_id=member_id, user_id=request.user.id)
        self.context = {'member': member, 'fights': fights}
        print(member.owner)
        return render(request, template_name=self.template_name, context=self.context)


class ViewMembers(View):
    template_name = 'member/add_entry.html'
    context = {}

    def get(self, request,  **kwargs):
        entry_list = []
        members_list = ''
        if request.GET['action'] == 'ALL':
            members = Members.objects.filter(user_id=request.user.id).order_by('-owner').values()
            for member in members:
                count = Entry.objects.filter(tournament_id=request.GET['tournament_id'], user_id=request.user.id, member_id=member['id']).count()
                entry_list.append({'id': member['id'], 'owner': member['owner'], 'count': count})
            members_list = list(entry_list)

        elif request.GET['action'] == 'SEARCH':
            members = Members.objects.filter(user_id=request.user.id, owner__contains=request.GET['keywords']).order_by('-owner').values()
            for member in members:
                count = Entry.objects.filter(tournament_id=request.GET['tournament_id'], user_id=request.user.id,
                                             member_id=member['id']).count()
                entry_list.append({'id': member['id'], 'owner': member['owner'], 'count': count})
            members_list = list(entry_list)
        elif request.GET['action'] == 'GET_MEMBER_INFO':
            member_id = request.GET['member_id']
            member = Members.objects.filter(user_id=request.user.id, id=member_id).values()
            members_list = list(member)

        return JsonResponse(members_list, safe=False)
