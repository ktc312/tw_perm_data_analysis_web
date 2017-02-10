#  -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render


# Create your views here.
def index(request):
    end_year = '2017'
    end_mon = '1'
    total_perm = '1000'
    approved_perm = '900'
    top_10_com_count = [['A', '1000', '10%'],
                        ['B', '900', '10%'],
                        ['C', '800', '10%'],
                        ['D', '700', '10%'],
                        ['E', '600', '10%'],
                        ['F', '500', '10%'],
                        ['G', '400', '10%'],
                        ['H', '300', '10%'],
                        ['I', '200', '10%'],
                        ['J', '100', '10%']]
    top_10_state_count = [['A', '1000', '10%'],
                        ['B', '900', '10%'],
                        ['C', '800', '10%'],
                        ['D', '700', '10%'],
                        ['E', '600', '10%'],
                        ['F', '500', '10%'],
                        ['G', '400', '10%'],
                        ['H', '300', '10%'],
                        ['I', '200', '10%'],
                        ['J', '100', '10%']]
    ny_perm = '500'
    ny_mean = '500'
    ny_median = '500'
    ny_std = '500'
    ny_min = '500'
    ny_max = '500'
    ny_salary_dis = [['<20,000', 10],
                     ['20,001 - 30,000', 11],
                     ['30,001 - 40,000', 15],
                     ['40,001 - 50,000', 20],
                     ['50,001 - 60,000', 25],
                     ['60,001 - 70,000', 30],
                     ['70,001 - 80,000', 45],
                     ['80,001 - 90,000', 35],
                     ['90,001 - 100,000', 30],
                     ['100,001 - 110,000', 20],
                     ['110,001 - 120,000', 11],
                     ['>120,001', 10]]
    years_mean_median = [['2007', '75', '65'],
                         ['2008', '50', '40'],
                         ['2009', '75', '65'],
                         ['2010', '50', '40'],
                         ['2011', '75', '65'],
                         ['2012', '100', '90'],
                         ['2013', '50', '60'],
                         ['2014', '75', '70'],
                         ['2015', '75', '65'],
                         ['2016', '100', '90']]
    top_10_state_mean = [['A', '75', '65'],
                         ['B', '50', '40'],
                         ['C', '75', '65'],
                         ['D', '50', '40'],
                         ['E', '75', '65'],
                         ['F', '100', '90'],
                         ['G', '50', '60'],
                         ['H', '75', '70'],
                         ['I', '75', '65'],
                         ['J', '100', '90']]
    top_state_name = 'unknown'
    top_state_median = '-9,999'
    last_update_time = '-99'
    context = {'end_year': end_year, 'end_mon': end_mon, 'total_perm': total_perm, 'approved_perm': approved_perm,
               'top_10_com_count': top_10_com_count, 'top_10_state_count': top_10_state_count, 'ny_perm': ny_perm,
               'ny_mean': ny_mean, 'ny_median': ny_median, 'ny_std': ny_std, 'ny_min': ny_min, 'ny_max': ny_max,
               'ny_salary_dis': ny_salary_dis, 'years_mean_median': years_mean_median,
               'top_10_state_mean': top_10_state_mean, 'top_state_name': top_state_name,
               'top_state_median': top_state_median}

    return render(request, 'main/index.html', context)


def qa_page(request):
    return render(request, 'main/qa_page.html')


def working(request):
    return render(request, 'main/working.html')
