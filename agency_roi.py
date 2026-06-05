<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Platinux Agency - ROI Calculator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8f7f4;
            color: #0f0f0f;
            overflow-x: hidden;
        }
        
        /* Custom Animations */
        @keyframes fadeUp {
            0% { opacity: 0; transform: translateY(30px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .animate-fade-up {
            opacity: 0;
            animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .delay-100 { animation-delay: 100ms; }
        .delay-200 { animation-delay: 200ms; }
        .delay-300 { animation-delay: 300ms; }

        .reveal-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease-out, transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .reveal-on-scroll.is-visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Pulse Highlight */
        @keyframes pulseHighlight {
            0% { box-shadow: 0 0 0 0 rgba(0, 196, 140, 0.3); }
            70% { box-shadow: 0 0 0 10px rgba(0, 196, 140, 0); }
            100% { box-shadow: 0 0 0 0 rgba(0, 196, 140, 0); }
        }
        .pulse-card {
            animation: pulseHighlight 2.5s infinite;
        }

        /* Custom Input Styling for Sliders */
        input[type=range] {
            -webkit-appearance: none;
            width: 100%;
            background: transparent;
        }
        input[type=range]::-webkit-slider-thumb {
            -webkit-appearance: none;
            height: 20px;
            width: 20px;
            border-radius: 50%;
            background: #00c48c;
            cursor: pointer;
            margin-top: -8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        input[type=range]::-webkit-slider-runnable-track {
            width: 100%;
            height: 4px;
            cursor: pointer;
            background: #e4e4e4;
            border-radius: 2px;
        }
        input[type=range]:focus {
            outline: none;
        }
    </style>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: '#00c48c',
                        dark: '#0f0f0f',
                        light: '#f8f7f4',
                        card: '#ffffff',
                        border: '#e4e4e4'
                    }
                }
            }
        }
    </script>
</head>
<body class="antialiased selection:bg-brand selection:text-white pb-20">

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8">
        <header class="bg-dark text-white rounded-3xl py-20 px-6 text-center shadow-xl animate-fade-up">
            <div class="inline-flex items-center gap-2 bg-white/10 border border-white/20 rounded-full px-4 py-1.5 text-sm text-gray-300 mb-6">
                <span>⚡</span> platinux.net/agency - ROI Calculator
            </div>
            <h1 class="text-4xl md:text-6xl font-bold tracking-tight mb-6 leading-tight">
                Stop scaling your sales team.<br>
                Scale your <span class="text-brand">lead flow.</span>
            </h1>
            <p class="text-lg md:text-xl text-gray-400 max-w-2xl mx-auto leading-relaxed">
                Platinux tracks founders and enterprises actively requesting custom development, SaaS builds, and design overhauls. Reach high-ticket clients before they post on Upwork.
            </p>
        </header>
    </div>

    <section class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
        <div class="mb-16 reveal-on-scroll">
            <span class="text-xs font-bold tracking-widest uppercase text-gray-500 mb-3 block">🗺 Your path to clients</span>
            <h2 class="text-3xl md:text-4xl font-bold text-dark mb-4 tracking-tight">From <em class="not-italic bg-brand/20 px-2 rounded">zero</em> to paid. In 4 steps.</h2>
            <p class="text-gray-600 text-lg max-w-2xl">Here's exactly how Platinux turns a business owner's post into money in your account — and why responding first is everything.</p>
        </div>

        <!-- Timeline Container -->
        <div class="relative wrap overflow-hidden p-2 md:p-10 h-full">
            <!-- Center Line (Desktop) / Left Line (Mobile) -->
            <div class="absolute border-opacity-100 border-gray-300 h-full border-2" style="left: 24px; md:left: 50%; transform: translateX(-50%);"></div>

            <!-- Step 1: Left -->
            <div class="mb-8 flex justify-between items-center w-full reveal-on-scroll">
                <div class="order-1 w-[40px] md:w-5/12"></div>
                <div class="z-20 flex items-center order-1 bg-white border-2 border-gray-200 w-12 h-12 rounded-full absolute" style="left: 24px; md:left: 50%; transform: translateX(-50%);">
                    <h1 class="mx-auto font-bold text-lg text-dark">1</h1>
                </div>
                <div class="order-1 bg-white rounded-2xl border border-border shadow-sm p-6 md:p-8 w-[calc(100%-60px)] md:w-5/12 ml-auto md:ml-0 transition-transform hover:-translate-y-1 hover:border-brand hover:shadow-lg hover:shadow-brand/10">
                    <span class="inline-flex items-center text-xs font-bold uppercase tracking-wide px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 mb-4">🔍 Intent</span>
                    <h3 class="font-bold text-xl mb-2 text-dark">Business owner posts online</h3>
                    <p class="text-gray-600 text-sm leading-relaxed mb-4">Somewhere on Reddit, LinkedIn, or Twitter, a real business owner types "looking for a web developer." It goes live publicly.</p>
                    <div class="bg-light border border-border rounded-lg p-3 flex gap-3 items-start">
                        <div class="w-2 h-2 rounded-full bg-brand mt-1.5 flex-shrink-0"></div>
                        <p class="text-xs text-gray-600"><strong>r/entrepreneur:</strong> "Need someone to build a site for my salon — budget $2,000, want it done this month."</p>
                    </div>
                </div>
            </div>

            <!-- Step 2: Right -->
            <div class="mb-8 flex justify-between items-center w-full flex-row md:flex-row-reverse reveal-on-scroll">
                <div class="order-1 w-[40px] md:w-5/12"></div>
                <div class="z-20 flex items-center order-1 bg-white border-2 border-gray-200 w-12 h-12 rounded-full absolute" style="left: 24px; md:left: 50%; transform: translateX(-50%);">
                    <h1 class="mx-auto font-bold text-lg text-dark">2</h1>
                </div>
                <div class="order-1 bg-white rounded-2xl border border-border shadow-sm p-6 md:p-8 w-[calc(100%-60px)] md:w-5/12 ml-auto md:mr-0 transition-transform hover:-translate-y-1 hover:border-brand hover:shadow-lg hover:shadow-brand/10">
                    <span class="inline-flex items-center text-xs font-bold uppercase tracking-wide px-3 py-1 rounded-full bg-orange-50 text-orange-700 mb-4">⚡ Speed</span>
                    <h3 class="font-bold text-xl mb-2 text-dark">Platinux alerts you instantly</h3>
                    <p class="text-gray-600 text-sm leading-relaxed mb-4">Our engine scans 7+ platforms 24/7. The second the post goes live, we capture it, verify it's a real business, and send you a real-time ping.</p>
                    <div class="bg-light border border-border rounded-lg p-3 flex gap-3 items-start">
                        <div class="w-2 h-2 rounded-full bg-brand mt-1.5 flex-shrink-0"></div>
                        <p class="text-xs text-gray-600"><strong>🔔 Alert:</strong> Salon owner · Reddit · Budget ~$2k · Posted 45s ago → <span class="text-brand font-semibold cursor-pointer">View post</span></p>
                    </div>
                </div>
            </div>

            <!-- Step 3: Left -->
            <div class="mb-8 flex justify-between items-center w-full reveal-on-scroll">
                <div class="order-1 w-[40px] md:w-5/12"></div>
                <div class="z-20 flex items-center order-1 bg-white border-2 border-gray-200 w-12 h-12 rounded-full absolute" style="left: 24px; md:left: 50%; transform: translateX(-50%);">
                    <h1 class="mx-auto font-bold text-lg text-dark">3</h1>
                </div>
                <div class="order-1 bg-white rounded-2xl border border-border shadow-sm p-6 md:p-8 w-[calc(100%-60px)] md:w-5/12 ml-auto md:ml-0 transition-transform hover:-translate-y-1 hover:border-brand hover:shadow-lg hover:shadow-brand/10">
                    <span class="inline-flex items-center text-xs font-bold uppercase tracking-wide px-3 py-1 rounded-full bg-blue-50 text-blue-700 mb-4">💬 Action</span>
                    <h3 class="font-bold text-xl mb-2 text-dark">You reply first</h3>
                    <p class="text-gray-600 text-sm leading-relaxed mb-4">You go directly to the post and respond. The business owner gets your message before they've even seen 10 other pitches. No platform middleman.</p>
                    <p class="text-xs text-gray-500 border-t border-border pt-3">Agencies who respond within 1 hour close at <strong>3× the rate</strong>.</p>
                </div>
            </div>

            <!-- Step 4: Right (Highlight) -->
            <div class="mb-8 flex justify-between items-center w-full flex-row md:flex-row-reverse reveal-on-scroll">
                <div class="order-1 w-[40px] md:w-5/12"></div>
                <div class="z-20 flex items-center order-1 bg-dark border-2 border-brand w-12 h-12 rounded-full absolute shadow-[0_0_15px_rgba(0,196,140,0.5)]" style="left: 24px; md:left: 50%; transform: translateX(-50%);">
                    <h1 class="mx-auto font-bold text-lg text-white">4</h1>
                </div>
                <div class="order-1 bg-dark rounded-2xl border-2 border-brand shadow-[0_8px_30px_rgba(0,196,140,0.15)] p-6 md:p-8 w-[calc(100%-60px)] md:w-5/12 ml-auto md:mr-0 relative overflow-hidden transition-transform hover:-translate-y-1">
                    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_left,_var(--tw-gradient-stops))] from-brand/20 via-transparent to-transparent"></div>
                    <div class="relative z-10">
                        <span class="inline-flex items-center text-xs font-bold uppercase tracking-wide px-3 py-1 rounded-full bg-brand/20 text-brand mb-4">💰 ROI</span>
                        <h3 class="font-bold text-xl mb-2 text-white">Project delivered. Money in.</h3>
                        <p class="text-gray-400 text-sm leading-relaxed mb-4">You build, deliver, and get paid. No Upwork commissions eating 20% of your income. Just you, the client, and the full project value.</p>
                        <div class="text-3xl font-bold text-brand mb-1">+$3,200</div>
                        <p class="text-xs text-gray-500 border-t border-gray-800 pt-3 mt-4">Platinux cost: <strong>$199/mo</strong> &nbsp;·&nbsp; Your ROI: <strong>Massive</strong></p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <div class="h-px bg-border w-full my-8"></div>

    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 reveal-on-scroll">
        <div class="mb-12">
            <span class="text-xs font-bold tracking-widest uppercase text-gray-500 mb-3 block">Agency Economics</span>
            <h2 class="text-3xl md:text-4xl font-bold text-dark mb-4 tracking-tight">Calculate your true net profit</h2>
            <p class="text-gray-600 text-lg max-w-2xl">Model your agency overhead based on a steady stream of <strong class="text-dark">100 verified hot leads per month</strong>.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
            <!-- Left: Inputs -->
            <div class="bg-white p-8 rounded-3xl border border-border shadow-sm">
                <h3 class="font-bold text-xl mb-6 border-b border-border pb-4">Your Agency Profile</h3>
                
                <div class="space-y-8">
                    <!-- Currency Toggle -->
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Currency</label>
                        <select id="currency-select" class="w-full bg-light border border-border rounded-lg px-4 py-3 text-sm focus:ring-2 focus:ring-brand focus:border-brand outline-none transition-all" onchange="updateCalculations()">
                            <option value="USD">USD ($)</option>
                            <option value="INR">INR (₹)</option>
                        </select>
                    </div>

                    <!-- Fixed Metric Alert -->
                    <div class="bg-emerald-50 border border-brand/30 rounded-xl p-4 flex items-center gap-4">
                        <div class="bg-brand text-white rounded-lg w-12 h-12 flex items-center justify-center font-bold text-xl shrink-0">100</div>
                        <div>
                            <h4 class="font-bold text-dark text-sm">Hot Leads per Month</h4>
                            <p class="text-xs text-gray-600 mt-1">Platinux delivers hundreds of leads. We are modeling your ROI conservatively on just 100 leads worked per month.</p>
                        </div>
                    </div>

                    <!-- Avg Project Size -->
                    <div>
                        <div class="flex justify-between mb-2">
                            <label class="text-sm font-medium text-gray-700">Average deal size</label>
                            <span id="deal-val" class="text-sm font-bold text-brand">$8,000</span>
                        </div>
                        <input type="range" id="deal-slider" min="2000" max="50000" step="1000" value="8000" oninput="updateCalculations()">
                    </div>

                    <!-- Close Rate -->
                    <div>
                        <div class="flex justify-between mb-2">
                            <label class="text-sm font-medium text-gray-700">Lead Close Rate</label>
                            <span id="close-val" class="text-sm font-bold text-brand">3%</span>
                        </div>
                        <input type="range" id="close-slider" min="1" max="20" step="1" value="3" oninput="updateCalculations()">
                        <p class="text-xs text-gray-500 mt-2">At 3%, you close 3 out of the 100 leads you pitch to.</p>
                    </div>

                    <!-- Net Margin -->
                    <div>
                        <div class="flex justify-between mb-2">
                            <label class="text-sm font-medium text-gray-700">Net Profit Margin</label>
                            <span id="margin-val" class="text-sm font-bold text-brand">40%</span>
                        </div>
                        <input type="range" id="margin-slider" min="10" max="80" step="5" value="40" oninput="updateCalculations()">
                        <p class="text-xs text-gray-500 mt-2">After paying your developers, software, and operational overhead.</p>
                    </div>
                </div>
            </div>

            <!-- Right: Outputs -->
            <div class="flex flex-col justify-center">
                <h3 class="font-bold text-xl mb-6">Your Monthly Results</h3>
                
                <div class="grid grid-cols-2 gap-4 mb-4">
                    <div class="bg-dark text-white rounded-2xl p-6 pulse-card shadow-lg border border-dark relative overflow-hidden">
                        <div class="absolute top-0 right-0 p-4 opacity-10">
                            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
                        </div>
                        <p class="text-sm text-gray-400 mb-1 font-medium">Agency ROI</p>
                        <p id="out-roi" class="text-3xl font-bold text-brand tracking-tight">4,724%</p>
                        <p id="out-roi-sub" class="text-xs text-gray-500 mt-2">Return on $199/mo</p>
                    </div>
                    
                    <div class="bg-white border border-border rounded-2xl p-6 shadow-sm transition hover:-translate-y-1">
                        <p class="text-sm text-gray-500 mb-1 font-medium">Gross Revenue / Mo</p>
                        <p id="out-rev" class="text-2xl font-bold text-dark tracking-tight">$24,000</p>
                        <p id="out-rev-sub" class="text-xs text-gray-400 mt-2">3 deals closed</p>
                    </div>
                </div>

                <div class="grid grid-cols-2 gap-4 mb-6">
                    <div class="bg-white border border-border rounded-2xl p-6 shadow-sm transition hover:-translate-y-1">
                        <p class="text-sm text-gray-500 mb-1 font-medium">Net Profit / Mo</p>
                        <p id="out-profit" class="text-2xl font-bold text-dark tracking-tight">$9,600</p>
                        <p id="out-profit-sub" class="text-xs text-gray-400 mt-2">After 60% dev overhead</p>
                    </div>
                    
                    <div class="bg-white border border-border rounded-2xl p-6 shadow-sm transition hover:-translate-y-1">
                        <p class="text-sm text-gray-500 mb-1 font-medium">Annual Net Profit</p>
                        <p id="out-annual" class="text-2xl font-bold text-dark tracking-tight">$112,812</p>
                        <p class="text-xs text-gray-400 mt-2">Minus Platinux fees</p>
                    </div>
                </div>

                <div class="bg-white border border-border border-l-4 border-l-brand rounded-r-xl p-5 text-sm text-gray-600 leading-relaxed shadow-sm">
                    <b>Minimal Risk.</b> You only need to close <b id="payback-clients" class="text-dark">0.06 deals</b> to completely cover your monthly Agency subscription from your <i>net profit</i> margin alone.
                </div>
            </div>
        </div>
    </section>

    <div class="h-px bg-border w-full my-8"></div>

    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 reveal-on-scroll">
        <div class="mb-12">
            <span class="text-xs font-bold tracking-widest uppercase text-gray-500 mb-3 block">12-Month Projection</span>
            <h2 class="text-3xl md:text-4xl font-bold text-dark mb-4 tracking-tight">Scaling Profit, Not Headcount</h2>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-5 gap-8">
            <div class="lg:col-span-3 bg-white p-6 rounded-3xl border border-border shadow-sm">
                <canvas id="projectionChart" height="250"></canvas>
            </div>
            <div class="lg:col-span-2 bg-white p-6 rounded-3xl border border-border shadow-sm flex flex-col items-center justify-center relative">
                <h3 class="text-sm font-bold text-gray-500 mb-4 absolute top-6 left-6 uppercase tracking-wide">Monthly Revenue Breakdown</h3>
                <div class="w-full max-w-[250px] mt-6">
                    <canvas id="pieChart"></canvas>
                </div>
                <div id="pie-center-text" class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center mt-4">
                    <!-- Injected via JS -->
                </div>
            </div>
        </div>
    </section>

    <div class="h-px bg-border w-full my-8"></div>

    <section class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-16 reveal-on-scroll">
        <div class="mb-12 text-center">
            <span class="text-xs font-bold tracking-widest uppercase text-gray-500 mb-3 block">Acquisition Comparison</span>
            <h2 class="text-3xl md:text-4xl font-bold text-dark tracking-tight">Platinux vs Paid Acquisition</h2>
        </div>

        <div class="bg-white border border-border rounded-2xl overflow-hidden shadow-sm">
            <div class="grid grid-cols-3 bg-dark text-white p-4 text-sm font-semibold">
                <div></div>
                <div>B2B Ads / Outbound SDR</div>
                <div class="text-brand">Platinux Agency</div>
            </div>
            <div class="grid grid-cols-3 p-4 border-b border-border items-center text-sm">
                <div class="text-gray-500 font-medium">Lead Intent</div>
                <div class="text-red-500 font-medium">Cold (Interruptive)</div>
                <div class="text-green-600 font-medium">Hot (Actively Asking)</div>
            </div>
            <div class="grid grid-cols-3 p-4 border-b border-border items-center text-sm">
                <div class="text-gray-500 font-medium">Cost to scale</div>
                <div class="text-red-500 font-medium">Higher spend = more leads</div>
                <div class="text-green-600 font-medium">100+ leads (Flat Rate)</div>
            </div>
            <div class="grid grid-cols-3 p-4 border-b border-border items-center text-sm">
                <div class="text-gray-500 font-medium">Lead Exclusivity</div>
                <div class="text-red-500 font-medium">Bidding against competitors</div>
                <div class="text-green-600 font-medium">You reach out first</div>
            </div>
            <div class="grid grid-cols-3 p-4 items-center text-sm">
                <div class="text-gray-500 font-medium">Annual Acquisition Cost</div>
                <div id="compare-sdr-cost" class="text-red-500 font-medium">$24,000</div>
                <div id="compare-plat-cost" class="text-green-600 font-medium bg-green-50 inline-block px-2 py-1 rounded w-max">$2,388 flat</div>
            </div>
        </div>
    </section>

    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 reveal-on-scroll">
        <div class="mb-12 text-center">
            <span class="text-xs font-bold tracking-widest uppercase text-gray-500 mb-3 block">Agency Plans</span>
            <h2 class="text-3xl md:text-4xl font-bold text-dark tracking-tight">One deal covers the year.</h2>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Pro -->
            <div class="bg-white border border-border rounded-3xl p-8 flex flex-col shadow-sm">
                <div class="text-xs text-gray-500 font-bold uppercase tracking-widest mb-3">Pro (Solo Devs)</div>
                <div id="price-pro" class="text-4xl font-bold text-dark mb-1">$79</div>
                <div class="text-sm text-gray-400 mb-6">/ mo</div>
                <ul class="text-sm text-gray-600 space-y-3 flex-grow">
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Unlimited leads</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Real-time alerts</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> 1 User Seat</li>
                    <li class="flex items-center gap-2 text-gray-400">— No team routing</li>
                    <li class="flex items-center gap-2 text-gray-400">— No CRM integrations</li>
                </ul>
            </div>

            <!-- Agency (Highlighted) -->
            <div class="bg-dark border border-dark rounded-3xl p-8 flex flex-col shadow-xl transform md:-translate-y-4 relative overflow-hidden">
                <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_rgba(0,196,140,0.15),_transparent)] pointer-events-none"></div>
                <div class="text-xs text-brand font-bold uppercase tracking-widest mb-3 relative z-10">Agency — Built for Teams</div>
                <div id="price-agency" class="text-4xl font-bold text-white mb-1 relative z-10">$199</div>
                <div id="price-agency-sub" class="text-sm text-gray-400 mb-6 relative z-10">/ mo · or $1,899/yr</div>
                <ul class="text-sm text-gray-300 space-y-3 flex-grow relative z-10">
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Everything in Pro</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> 5 Team Seats (Sales/SDR)</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Slack / Discord Routing</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> HubSpot / Salesforce Sync</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> API Access</li>
                </ul>
                <button class="mt-8 w-full bg-brand hover:bg-emerald-500 text-white font-bold py-3 rounded-xl transition shadow-lg shadow-brand/20 relative z-10">Start 14-Day Free Trial</button>
            </div>

            <!-- Enterprise -->
            <div class="bg-white border border-border rounded-3xl p-8 flex flex-col shadow-sm">
                <div class="text-xs text-gray-500 font-bold uppercase tracking-widest mb-3">Enterprise Scale</div>
                <div id="price-scale" class="text-4xl font-bold text-dark mb-1">$499+</div>
                <div class="text-sm text-gray-400 mb-6">/ mo</div>
                <ul class="text-sm text-gray-600 space-y-3 flex-grow">
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Unlimited Team Seats</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Custom Data Pipelines</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Dedicated Account Rep</li>
                    <li class="flex items-center gap-2"><span class="text-brand">✓</span> Whitelabel Reports</li>
                </ul>
            </div>
        </div>
    </section>

    <script>
        // --- Scroll Reveal Animation ---
        document.addEventListener("DOMContentLoaded", () => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                    }
                });
            }, { threshold: 0.1 });

            document.querySelectorAll('.reveal-on-scroll').forEach((el) => {
                observer.observe(el);
            });
            
            // Initialize calculator
            updateCalculations();
        });

        // --- Global Variables for Charts ---
        let lineChartInstance = null;
        let pieChartInstance = null;

        // --- Formatter Utility ---
        function formatMoney(amount, currency) {
            const symbol = currency === 'INR' ? '₹' : '$';
            if (currency === 'INR') {
                if (amount >= 100000) return symbol + (amount / 100000).toFixed(1) + 'L';
                return symbol + Math.round(amount).toLocaleString('en-IN');
            } else {
                if (amount >= 1000) return symbol + (amount / 1000).toFixed(1) + 'k';
                return symbol + Math.round(amount).toLocaleString('en-US');
            }
        }

        // --- Main Calculation Logic ---
        function updateCalculations() {
            const currency = document.getElementById('currency-select').value;
            const isINR = currency === 'INR';
            const symbol = isINR ? '₹' : '$';
            
            // Constants
            const leadsPerMonth = 100; // Fixed metric as requested
            const planCost = isINR ? 17999 : 199;
            const sdrCost = isINR ? 150000 : 2000;
            
            // Update Slider Ranges based on Currency
            const dealSlider = document.getElementById('deal-slider');
            if (isINR && dealSlider.max !== "2000000") {
                dealSlider.min = 50000; dealSlider.max = 2000000; dealSlider.step = 50000; dealSlider.value = 400000;
            } else if (!isINR && dealSlider.max !== "50000") {
                dealSlider.min = 2000; dealSlider.max = 50000; dealSlider.step = 1000; dealSlider.value = 8000;
            }

            // Get Input Values
            const avgProject = parseFloat(dealSlider.value);
            const closeRate = parseFloat(document.getElementById('close-slider').value);
            const margin = parseFloat(document.getElementById('margin-slider').value);

            // Update Input Labels
            document.getElementById('deal-val').innerText = isINR ? formatMoney(avgProject, 'INR') : formatMoney(avgProject, 'USD');
            document.getElementById('close-val').innerText = closeRate + '%';
            document.getElementById('margin-val').innerText = margin + '%';

            // Math
            const clientsPerMonth = leadsPerMonth * (closeRate / 100);
            const monthlyRevenue = clientsPerMonth * avgProject;
            const monthlyOverhead = monthlyRevenue * (1 - (margin / 100));
            const monthlyProfit = monthlyRevenue - monthlyOverhead;
            const netGain = monthlyProfit - planCost;
            const roiX = planCost > 0 ? Math.round((monthlyProfit / planCost) * 100) : 0;
            const annualProfit = netGain * 12;

            // Update DOM Outputs
            document.getElementById('out-roi').innerText = roiX.toLocaleString() + '%';
            document.getElementById('out-roi-sub').innerText = `Return on ${symbol}${planCost.toLocaleString()}/mo`;
            
            document.getElementById('out-rev').innerText = formatMoney(monthlyRevenue, currency);
            document.getElementById('out-rev-sub').innerText = `${clientsPerMonth % 1 === 0 ? clientsPerMonth : clientsPerMonth.toFixed(1)} deals closed`;
            
            document.getElementById('out-profit').innerText = formatMoney(monthlyProfit, currency);
            document.getElementById('out-profit-sub').innerText = `After ${100 - margin}% dev overhead`;
            
            document.getElementById('out-annual').innerText = formatMoney(annualProfit, currency);

            const paybackClients = planCost / (avgProject * (margin / 100));
            document.getElementById('payback-clients').innerText = paybackClients < 1 ? "< 1 deal" : paybackClients.toFixed(1) + " deals";

            // Update Comparison Table
            document.getElementById('compare-sdr-cost').innerText = formatMoney(sdrCost * 12, currency);
            document.getElementById('compare-plat-cost').innerText = formatMoney(planCost * 12, currency) + " flat";

            // Update Pricing Block
            if (isINR) {
                document.getElementById('price-pro').innerText = "₹1,999";
                document.getElementById('price-agency').innerText = "₹17,999";
                document.getElementById('price-agency-sub').innerText = "/ mo · or ₹160,000/yr";
                document.getElementById('price-scale').innerText = "Custom";
            } else {
                document.getElementById('price-pro').innerText = "$79";
                document.getElementById('price-agency').innerText = "$199";
                document.getElementById('price-agency-sub').innerText = "/ mo · or $1,899/yr";
                document.getElementById('price-scale').innerText = "$499+";
            }

            // Update Charts
            updateCharts(monthlyProfit, planCost, sdrCost, monthlyOverhead, currency, margin);
        }

        function updateCharts(monthlyProfit, planCost, sdrCost, monthlyOverhead, currency, margin) {
            const months = Array.from({length: 12}, (_, i) => `M${i+1}`);
            const sdrData = Array.from({length: 12}, (_, i) => Math.max(0, (monthlyProfit * (1 + 0.02*i)) - sdrCost));
            const platData = Array.from({length: 12}, (_, i) => Math.max(0, (monthlyProfit * (1 + 0.05*i)) - planCost));

            // Line Chart
            const ctxLine = document.getElementById('projectionChart').getContext('2d');
            if (lineChartInstance) {
                lineChartInstance.data.datasets[0].data = sdrData;
                lineChartInstance.data.datasets[1].data = platData;
                lineChartInstance.update();
            } else {
                lineChartInstance = new Chart(ctxLine, {
                    type: 'line',
                    data: {
                        labels: months,
                        datasets: [
                            {
                                label: 'Via Ads/Outbound SDR',
                                data: sdrData,
                                borderColor: '#e24b4a',
                                borderDash: [5, 5],
                                borderWidth: 2,
                                pointRadius: 3,
                                fill: false,
                                tension: 0.3
                            },
                            {
                                label: 'Via Platinux Agency',
                                data: platData,
                                borderColor: '#00c48c',
                                backgroundColor: 'rgba(0, 196, 140, 0.1)',
                                borderWidth: 3,
                                pointRadius: 4,
                                fill: true,
                                tension: 0.3
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        interaction: { intersect: false, mode: 'index' },
                        plugins: {
                            legend: { position: 'top', align: 'start', labels: { usePointStyle: true, boxWidth: 8, font: { family: 'Inter' } } },
                            tooltip: { backgroundColor: '#0f0f0f', titleFont: { family: 'Inter' }, bodyFont: { family: 'Inter' }, padding: 12 }
                        },
                        scales: {
                            y: { beginAtZero: true, grid: { color: '#f0eeea' }, border: { display: false }, ticks: { font: { family: 'Inter' }, callback: function(val) { return formatMoney(val, currency); } } },
                            x: { grid: { display: false }, border: { display: false }, ticks: { font: { family: 'Inter' } } }
                        }
                    }
                });
            }

            // Pie Chart
            const trueProfit = Math.max(0, monthlyProfit - planCost);
            const pieData = [trueProfit, monthlyOverhead, planCost];
            const ctxPie = document.getElementById('pieChart').getContext('2d');
            
            if (pieChartInstance) {
                pieChartInstance.data.datasets[0].data = pieData;
                pieChartInstance.data.labels[1] = `Dev/Overhead (${100-margin}%)`;
                pieChartInstance.update();
            } else {
                pieChartInstance = new Chart(ctxPie, {
                    type: 'doughnut',
                    data: {
                        labels: ['Agency Net Profit', `Dev/Overhead (${100-margin}%)`, 'Platinux Cost'],
                        datasets: [{
                            data: pieData,
                            backgroundColor: ['#00c48c', '#e4e4e4', '#0f0f0f'],
                            borderWidth: 2,
                            borderColor: '#ffffff'
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        cutout: '70%',
                        plugins: {
                            legend: { display: false },
                            tooltip: { backgroundColor: '#0f0f0f', padding: 12, bodyFont: { family: 'Inter' }, callbacks: { label: function(context) { return ' ' + context.label + ': ' + formatMoney(context.raw, currency); } } }
                        }
                    }
                });
            }

            // Update text in the middle of doughnut chart
            document.getElementById('pie-center-text').innerHTML = `
                <div class="text-xl font-bold text-dark leading-none">${formatMoney(trueProfit, currency)}</div>
                <div class="text-[10px] text-gray-500 font-medium uppercase mt-1">True Profit</div>
            `;
        }
    </script>
</body>
</html>
