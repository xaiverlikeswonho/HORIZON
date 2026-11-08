const pages={
 overview:["Overview","Your server at a glance. Configure HORIZON from one place."],
 commands:["Commands","Browse the planned command action registry."],
 members:["Members","Member tools and permission workflows."],
 roles:["Roles","Configure role-management preferences."],
 moderation:["Moderation","Manage moderation tools and staff permissions."],
 automod:["Auto moderation","Configure automated server protection."],
 logs:["Audit logs","Choose which server events should be recorded."],
 welcome:["Welcome & goodbye","Customize your member join and leave experience."],
 embeds:["Embed builder","Create and preview Discord-style embeds."],
 settings:["Bot settings","Configure HORIZON's identity and behavior."]
};
const nav=document.getElementById('navigation');
function go(page){if(!pages[page])return;document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));document.getElementById('page-'+page)?.classList.add('active');document.querySelectorAll('.nav-item').forEach(b=>b.classList.toggle('active',b.dataset.page===page));document.getElementById('crumb').textContent=pages[page][0];document.getElementById('pageTitle').textContent=pages[page][0];document.getElementById('pageDesc').textContent=pages[page][1];document.getElementById('sidebar').classList.remove('open');window.scrollTo({top:0,behavior:'smooth'});}
nav.addEventListener('click',e=>{const b=e.target.closest('[data-page]');if(b)go(b.dataset.page)});
document.querySelectorAll('[data-go]').forEach(b=>b.addEventListener('click',()=>go(b.dataset.go)));
document.getElementById('menuBtn').addEventListener('click',()=>document.getElementById('sidebar').classList.toggle('open'));
document.getElementById('themeBtn').addEventListener('click',()=>{document.body.classList.toggle('light');localStorage.setItem('hz-light',document.body.classList.contains('light')?'1':'0')});
if(localStorage.getItem('hz-light')==='1')document.body.classList.add('light');
let toastTimer;function toast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');clearTimeout(toastTimer);toastTimer=setTimeout(()=>t.classList.remove('show'),2400)}
document.querySelectorAll('.save-btn').forEach(btn=>btn.addEventListener('click',()=>{const page=btn.closest('.page');const values={};page.querySelectorAll('[data-setting]').forEach(el=>{values[el.dataset.setting]=el.type==='checkbox'?el.checked:el.value});const all=JSON.parse(localStorage.getItem('horizon-settings')||'{}');Object.assign(all,values);localStorage.setItem('horizon-settings',JSON.stringify(all));toast('Preferences saved on this device. Discord sync is not connected yet.')}));
const saved=JSON.parse(localStorage.getItem('horizon-settings')||'{}');document.querySelectorAll('[data-setting]').forEach(el=>{const v=saved[el.dataset.setting];if(v!==undefined){if(el.type==='checkbox')el.checked=!!v;else el.value=v}});
const categories=[
["Core & utility","Slash","Help, bot info, ping, server info, user info, uptime, and configuration."],
["Moderation","Slash","Warn, timeout, kick, ban, unban, purge, slowmode, and case history."],
["Moderation","Prefix","Fast prefix-based moderation shortcuts and case lookups."],
["Member management","Slash","Member search, profiles, notes, joins, leaves, and member statistics."],
["Roles & permissions","Slash","Role assignment, role menus, staff roles, and permission checks."],
["Server configuration","Prefix","Prefix settings, welcome setup, log channels, and module toggles."],
["Auto moderation","Slash","Spam rules, invite filters, blocked words, and safety controls."],
["Engagement","Slash","Polls, suggestions, reminders, starboard, and community activities."],
["Information","Prefix","Server details, channel details, role details, and command help."],
["Owner & maintenance","Slash","Bot status, maintenance mode, backups, diagnostics, and owner tools."]
];
const list=document.getElementById('commandList');function renderCommands(){if(!list)return;const q=(document.getElementById('commandSearch').value||'').toLowerCase();const type=document.getElementById('commandType').value;list.innerHTML='';categories.filter(c=>(c.join(' ').toLowerCase().includes(q))&&(type==='all'||c[1]===type)).forEach(c=>{const row=document.createElement('div');row.className='command-row';const left=document.createElement('div');const b=document.createElement('b');b.textContent=c[0];const sm=document.createElement('small');sm.textContent=c[2];left.append(b,sm);const tag=document.createElement('span');tag.className='command-type';tag.textContent=c[1].toUpperCase();row.append(left,tag);list.append(row)});if(!list.children.length)list.innerHTML='<div class="empty-state">No matching categories.</div>'}
document.getElementById('commandSearch')?.addEventListener('input',renderCommands);document.getElementById('commandType')?.addEventListener('change',renderCommands);renderCommands();
document.getElementById('quickAction').addEventListener('click',()=>{go('moderation');toast('Choose a moderation setting to configure.')});
['embedTitle','embedDescription','embedFooter'].forEach(id=>document.getElementById(id).addEventListener('input',()=>{document.getElementById('previewTitle').textContent=document.getElementById('embedTitle').value||'Embed title';document.getElementById('previewDescription').textContent=document.getElementById('embedDescription').value;document.getElementById('previewFooter').textContent=document.getElementById('embedFooter').value}));
