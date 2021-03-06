#  -*- coding: utf-8 -*-
# coding: utf-8
from django.shortcuts import render
import web_functions
import sys


# Create your views here.
def index(request):
    end_year = '-99'
    end_mon = '-99'
    total_perm = '-99'
    approved_perm = '-99'
    top_10_com_count = [['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99']]
    top_10_state_count = [['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99'],
                          ['-99', '-99', '-99']]
    ny_perm = '-99'
    ny_mean = '-99'
    ny_median = '-99'
    ny_std = '-99'
    ny_min = '-99'
    ny_max = '-99'
    ny_salary_dis = [['< 20,000', -99],
                     ['20,001 - 30,000', -99],
                     ['30,001 - 40,000', -99],
                     ['40,001 - 50,000', -99],
                     ['50,001 - 60,000', -99],
                     ['60,001 - 70,000', -99],
                     ['70,001 - 80,000', -99],
                     ['80,001 - 90,000', -99],
                     ['90,001 - 100,000', -99],
                     ['100,001 - 110,000', -99],
                     ['110,001 - 120,000', -99],
                     ['120,001 - 130,000', -99],
                     ['130,001 - 140,000', -99],
                     ['140,001 - 150,000', -99],
                     ['> 150,001', -99]]
    years_mean_median = [['2007', '-99', '-99'],
                         ['2008', '-99', '-99'],
                         ['2009', '-99', '-99'],
                         ['2010', '-99', '-99'],
                         ['2011', '-99', '-99'],
                         ['2012', '-99', '-99'],
                         ['2013', '-99', '-99'],
                         ['2014', '-99', '-99'],
                         ['2015', '-99', '-99'],
                         ['2016', '-99', '-99'],
                         ['2017', '-99', '-99']]
    top_10_state_mean = [['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99'],
                         ['-99', '-99', '-99']]
    top_state_name = '-99'
    top_state_median = '-99'
    last_update_time = '-99'
    context = {'end_year': end_year, 'end_mon': end_mon, 'total_perm': total_perm, 'approved_perm': approved_perm,
               'top_10_com_count': top_10_com_count, 'top_10_state_count': top_10_state_count, 'ny_perm': ny_perm,
               'ny_mean': ny_mean, 'ny_median': ny_median, 'ny_std': ny_std, 'ny_min': ny_min, 'ny_max': ny_max,
               'ny_salary_dis': ny_salary_dis, 'years_mean_median': years_mean_median,
               'top_10_state_mean': top_10_state_mean, 'top_state_name': top_state_name,
               'top_state_median': top_state_median, 'last_update_time': last_update_time}

    try:
        summarize_main = web_functions.read_summarize_main()
        context['total_perm'] = summarize_main[0].split('.')[0]
        context['approved_perm'] = summarize_main[1].split('.')[0]
        context['ny_perm'] = summarize_main[2].split('.')[0]
        context['end_year'] = summarize_main[3]
        context['end_mon'] = summarize_main[4]
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        context['top_10_com_count'] = web_functions.read_top_ten_com()
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        context['top_10_state_count'] = web_functions.read_top_ten_state()
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        summarize_ny = web_functions.read_summarize_ny()
        context['ny_mean'] = summarize_ny[0]
        context['ny_std'] = summarize_ny[1]
        context['ny_median'] = summarize_ny[2]
        context['ny_min'] = summarize_ny[3]
        context['ny_max'] = summarize_ny[4]
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        context['ny_salary_dis'] = web_functions.read_ny_salary_all()
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        context['last_update_time'] = web_functions.read_csv_to_list('data/update_log.csv')[0][1]
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        context['years_mean_median'] = web_functions.read_all_yr_means()
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        context['top_10_state_mean'] = web_functions.read_top_10_state_mean()
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    try:
        top_median_state = web_functions.read_top_median_state()
        context['top_state_name'] = top_median_state[0]
        context['top_state_median'] = top_median_state[1]
    except:
        e = sys.exc_info()[0]
        print "<p>Error: %s</p>" % e

    return render(request, 'main/index.html', context)


def qa_page(request):
    return render(request, 'main/qa_page.html')


def top_com_yr(request):
    start_year = -99
    start_mon = 1
    end_year = -99
    end_mon = 12
    total_perm = -99
    approved_perm = -99
    top_10_com_count = [['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99']]
    yr_list = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    context = {'start_year': start_year, 'start_mon': start_mon, 'end_year': end_year, 'end_mon': end_mon,
               'total_perm': total_perm, 'approved_perm': approved_perm, 'top_10_com_count': top_10_com_count,
               'yr_list': yr_list}

    try:
        # get user input
        user_start_yr = request.GET['start_yr']
        user_end_yr = request.GET['end_yr']
        context['start_year'] = user_start_yr
        context['end_year'] = user_end_yr

    except:
        context['start_year'] = 2007
        context['end_year'] = 2017

    summarize_main = web_functions.read_summarize_main()
    last_yr = int(summarize_main[3])
    last_mon = int(summarize_main[4])
    if context['end_year'] == last_yr:
        context['end_mon'] = last_mon

    return render(request, 'main/top_com_yr.html', context)


def top_state_yr(request):
    start_year = -99
    start_mon = 1
    end_year = -99
    end_mon = 12
    total_perm = -99
    approved_perm = -99
    top_10_state_count = [['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99'],
                        ['-99', '-99', '-99']]
    yr_list = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    context = {'start_year': start_year, 'start_mon': start_mon, 'end_year': end_year, 'end_mon': end_mon,
               'total_perm': total_perm, 'approved_perm': approved_perm, 'top_10_state_count': top_10_state_count,
               'yr_list': yr_list}

    try:
        # get user input
        user_start_yr = request.GET['start_yr']
        user_end_yr = request.GET['end_yr']
        context['start_year'] = user_start_yr
        context['end_year'] = user_end_yr

    except:
        context['start_year'] = 2007
        context['end_year'] = 2017

    summarize_main = web_functions.read_summarize_main()
    last_yr = int(summarize_main[3])
    last_mon = int(summarize_main[4])
    if context['end_year'] == last_yr:
        context['end_mon'] = last_mon

    return render(request, 'main/top_state_yr.html', context)


def by_area_yr(request):
    area_name = "New York Metro"
    start_year = -99
    start_mon = 1
    end_year = -99
    end_mon = 12
    approved_perm = '-99'
    ny_perm = '-99'
    ny_mean = '-99'
    ny_median = '-99'
    ny_std = '-99'
    ny_min = '-99'
    ny_max = '-99'
    ny_salary_dis = [['< 20,000', -99],
                     ['20,001 - 30,000', -99],
                     ['30,001 - 40,000', -99],
                     ['40,001 - 50,000', -99],
                     ['50,001 - 60,000', -99],
                     ['60,001 - 70,000', -99],
                     ['70,001 - 80,000', -99],
                     ['80,001 - 90,000', -99],
                     ['90,001 - 100,000', -99],
                     ['100,001 - 110,000', -99],
                     ['110,001 - 120,000', -99],
                     ['120,001 - 130,000', -99],
                     ['130,001 - 140,000', -99],
                     ['140,001 - 150,000', -99],
                     ['> 150,001', -99]]
    yr_list = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    context = {'area_name': area_name, 'start_year': start_year, 'start_mon': start_mon, 'end_year': end_year,
               'end_mon': end_mon, 'approved_perm': approved_perm, 'ny_perm': ny_perm, 'ny_mean': ny_mean,
               'ny_median': ny_median, 'ny_std': ny_std, 'ny_min': ny_min, 'ny_max': ny_max,
               'ny_salary_dis': ny_salary_dis, 'yr_list': yr_list}

    try:
        # get user input
        user_start_yr = request.GET['start_yr']
        user_end_yr = request.GET['end_yr']
        context['start_year'] = user_start_yr
        context['end_year'] = user_end_yr
    except:
        context['start_year'] = 2007
        context['end_year'] = 2017

    summarize_main = web_functions.read_summarize_main()
    last_yr = int(summarize_main[3])
    last_mon = int(summarize_main[4])
    if context['end_year'] == last_yr:
        context['end_mon'] = last_mon

    return render(request, 'main/by_area_yr.html', context)


def by_yr_more(request):
    years_mean_median = [['2007', '-99', '-99'],
                         ['2008', '-99', '-99'],
                         ['2009', '-99', '-99'],
                         ['2010', '-99', '-99'],
                         ['2011', '-99', '-99'],
                         ['2012', '-99', '-99'],
                         ['2013', '-99', '-99'],
                         ['2014', '-99', '-99'],
                         ['2015', '-99', '-99'],
                         ['2016', '-99', '-99'],
                         ['2017', '-99', '-99']]
    start_year = -99
    start_mon = 1
    end_year = 2017
    end_mon = 12
    approved_perm = '-99'
    context = {'years_mean_median': years_mean_median, 'start_year': start_year, 'start_mon': start_mon,
               'end_year': end_year, 'end_mon': end_mon, 'approved_perm': approved_perm}

    summarize_main = web_functions.read_summarize_main()
    last_yr = int(summarize_main[3])
    last_mon = int(summarize_main[4])
    if context['end_year'] == last_yr:
        context['end_mon'] = last_mon

    return render(request, 'main/by_yr_more.html', context)


def by_state_more(request):
    years_mean_median = [['2007', '-99', '-99'],
                         ['2008', '-99', '-99'],
                         ['2009', '-99', '-99'],
                         ['2010', '-99', '-99'],
                         ['2011', '-99', '-99'],
                         ['2012', '-99', '-99'],
                         ['2013', '-99', '-99'],
                         ['2014', '-99', '-99'],
                         ['2015', '-99', '-99'],
                         ['2016', '-99', '-99'],
                         ['2017', '-99', '-99']]
    start_year = -99
    start_mon = 1
    end_year = 2017
    end_mon = 12
    approved_perm = '-99'
    default_state = 'Oregon'
    state_list = []
    context = {'years_mean_median': years_mean_median, 'start_year': start_year, 'start_mon': start_mon,
               'end_year': end_year, 'end_mon': end_mon, 'approved_perm': approved_perm,
               'default_state': default_state, 'state_list': state_list}

    summarize_main = web_functions.read_summarize_main()
    last_yr = int(summarize_main[3])
    last_mon = int(summarize_main[4])
    if context['end_year'] == last_yr:
        context['end_mon'] = last_mon

    context['state_list'] = web_functions.get_state_list()

    return render(request, 'main/by_state_more.html', context)


def working(request):
    return render(request, 'main/working.html')
