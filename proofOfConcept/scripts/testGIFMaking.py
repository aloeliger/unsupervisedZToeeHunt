#!/usr/bin/env python3

import ROOT

theCanvas = ROOT.TCanvas()
theCanvas.SetGrid()

ROOT.gBenchmark.Start("hsum")

total = ROOT.TH1F('total', 'total distribution', 100, -4, 4)
main = ROOT.TH1F('main', 'main contributor', 100, -4, 4)
s1 = ROOT.TH1F('s1', 'this is the first signal', 100, -4, 4)
s2 = ROOT.TH1F('s2', 'this is the second signal', 100, -4, 4)
total.Sumw2()
total.SetMarkerStyle(21)
total.SetMarkerSize(0.7)
main.SetFillColor(16)
s1.SetFillColor(42)
s2.SetFillColor(46)

ROOT.gRandom.SetSeed(1234)
kUpdate = 500
gifcnt = 0
for i in range(10000):
    xmain = ROOT.gRandom.Gaus(-1,1.5)
    xs1 = ROOT.gRandom.Gaus(-0.5,0.5)
    xs2 = ROOT.gRandom.Gaus(1,0.15)
    main.Fill(xmain)
    s1.Fill(xs1,0.3)
    s2.Fill(xs2,0.2)
    total.Fill(xmain)
    total.Fill(xs1,0.3)
    total.Fill(xs2,0.2)
    if (i != 0 and i%kUpdate == 0):
        stack = ROOT.THStack('stack','')
        stack.Add(main, 'HIST')
        stack.Add(s1, 'HIST')
        stack.Add(s2, 'HIST')
        stack.Draw()
        total.Draw('same e1p')
    
        theCanvas.Modified
        theCanvas.Update()
        theCanvas.Print('hsumanim.gif+100')
        print(f'i = {i}')
total.Draw('sameaxis')
theCanvas.Modified()
theCanvas.Print('hsumanim.gif++')

ROOT.gBenchmark.Show('hsum')