from django.shortcuts import render, get_object_or_404, redirect
from partners.models import Partner
from partners.models import PartnerKnown

from .forms import PartnerForm
from .forms import PartnerKnownForm

from django.http import JsonResponse


def partner_list(request):
    partners = Partner.objects.all()
    return render(
        request,
        'partners/partner_list.html', {
            'partners': partners
        })


def partner_detail(request, pk):
    partner = get_object_or_404(Partner, pk=pk)

    #partnerknowns = PartnerKnown.objects.all()
    partnerknowns = PartnerKnown.objects.filter(partner=partner.pk)
    seen_list = PartnerKnown.SEEN_LIST

    return render(
        request,
        'partners/partner_detail.html', {
            'partner': partner,
            'partnerknowns': partnerknowns,
            'seen_list': seen_list
        })

    if request.method == "POST":
        partnerform = PartnerForm(request.POST, instance=partner)

        if partnerform.is_valid():
            partner = form.save(commit=False)
            partner.user = request.user
            partner.save()
            return redirect('partner_detail', pk=partner.pk)

    else:
        form = PartnerForm(instance=partner)

    return render(request, 'partners/partner_detail.html', {'form': form})


def partner_add(request):
    if request.method == "POST":
        partnerform = PartnerForm(request.POST)

        if partnerform.is_valid():
            partner = partnerform.save(commit=False)
            partner.user = request.user
            partner.save()
            return redirect(
                'partner_detail',
                pk=partner.pk
            )
    else:
        partnerform = PartnerForm()

    return render(request, 'partners/partner_edit.html', {'partnerform': partnerform})


def partner_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    partnerknown = PartnerKnown.objects.filter(partner=pk)

    if request.method == "POST":
        partnerform = PartnerForm(request.POST, instance=partner)
        partnerknownform = PartnerKnownForm(request.POST, instance=partner)

        if partnerform.is_valid():
            partner = partnerform.save()
            partner.user = request.user
            partner.save()
#            partnerknownform.save_m2m()


            return redirect('partner_detail', pk=partner.pk)
    else:
        partnerform = PartnerForm(instance=partner)
        partnerknownform = PartnerKnownForm()

    return render(request, 'partners/partner_edit.html', {
        'partnerform': partnerform,
        'partnerknownform': partnerknownform
    })
