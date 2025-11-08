🌸 Anna Beauty Studio — Sistema de Agendamentos

Um site moderno e responsivo para agendamentos de estética facial, lash design e beleza feminina, com confirmação automática via WhatsApp 💬
Projeto construído em Django + Celery, com mensagens personalizadas no melhor estilo: leve, divertida e com um toque de glamour ✨

💎 Estrutura do projeto
AnnaBeauty/
├── anna_beauty_simple/   ← versão com wa.me (sem custo)
└── anna_beauty_pro/      ← versão com Twilio API (envio automático)

🚀 1. Funcionalidades Principais

✅ Agendamento online com confirmação via WhatsApp
✅ Mensagens divertidas e femininas 💋
✅ Fila Celery para envio assíncrono de mensagens
✅ Proteção contra spam (Google reCAPTCHA)
✅ Bloqueio de horários sobrepostos (atomic lock)
✅ Página “Minhas Reservas” com contagem regressiva ✨
✅ Design responsivo (Bootstrap 5)
✅ Compatível com Render e PostgreSQL

🧰 2. Instalação local (ambas as versões)

1️⃣ Clone o repositório:

git clone https://github.com/<seu_usuario>/AnnaBeauty.git
cd AnnaBeauty/anna_beauty_simple


2️⃣ Crie e ative o ambiente virtual:

python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)


3️⃣ Instale as dependências:

pip install -r requirements.txt


4️⃣ Configure o ambiente:

cp .env.example .env


Edite o .env com:

SECRET_KEY=coloque_uma_chave
DEBUG=1
DATABASE_URL=sqlite:///db.sqlite3
RECAPTCHA_SITE_KEY=sua_site_key
RECAPTCHA_SECRET_KEY=sua_secret_key


5️⃣ Faça as migrações:

python manage.py makemigrations
python manage.py migrate


6️⃣ Inicie o servidor:

python manage.py runserver


7️⃣ Inicie o Celery (em outro terminal):

celery -A anna_beauty worker -l info


Acesse: 👉 http://127.0.0.1:8000

💬 3. Diferença entre as versões
Versão	Confirmação de agendamento	Requisitos
💖 anna_beauty_simple	Gera link wa.me pra o cliente abrir no WhatsApp	Nenhuma conta externa
💎 anna_beauty_pro	Envia mensagens automáticas via Twilio API	Conta Twilio verificada
✨ 4. Configuração do Twilio (versão PRO)

1️⃣ Crie uma conta gratuita no Twilio
.
2️⃣ Entre no painel e copie:

ACCOUNT SID

AUTH TOKEN

Número sandbox (ex: whatsapp:+1415XXXXXXX)

3️⃣ Configure o .env:

TWILIO_ACCOUNT_SID=ACxxxxxx
TWILIO_AUTH_TOKEN=yyyyyy
TWILIO_WHATSAPP_FROM=whatsapp:+1415XXXXXXX
PROFESSIONAL_WHATSAPP=whatsapp:+5512991613940


4️⃣ Envie “join <código_sandbox>” para o número Twilio, pra ativar o sandbox.

🪄 Pronto, gata! Agora, assim que alguém marcar um horário:

A cliente recebe confirmação no WhatsApp 💅

A profissional recebe notificação do novo agendamento 💖

☁️ 5. Deploy no Render

1️⃣ Suba o código pro GitHub.
2️⃣ Crie um serviço Web no Render → escolha o repositório.
3️⃣ Adicione variáveis de ambiente:

PYTHON_VERSION=3.11
DJANGO_SETTINGS_MODULE=anna_beauty.settings
DATABASE_URL=<URL do banco PostgreSQL do Render>
SECRET_KEY=<chave segura>
REDIS_URL=<url do Redis>


(se estiver usando a versão PRO, adicione as variáveis Twilio também)

4️⃣ Crie um serviço Worker com:

celery -A anna_beauty worker -l info

🧠 6. Personalização fácil

🎨 Mude cores, fontes e ícones no arquivo:
bookings/static/css/custom.css

🖼️ Atualize os textos dos templates HTML (pasta bookings/templates/):

home.html → texto da página inicial

book.html → formulário de agendamento

confirmation.html → mensagem pós-agendamento

my_appointments.html → lista das reservas

🔒 7. Segurança & Boas práticas

✔️ Nunca suba o arquivo .env pro GitHub.
✔️ Use DEBUG=0 em produção.
✔️ Gere SECRET_KEY nova com:

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


✔️ Proteja os formulários com reCAPTCHA (já implementado).
✔️ Configure HTTPS no Render (automático com domínio personalizado).

💋 8. Créditos e Licença

Criado com amor, café e brilho por você ☕✨
Desenvolvido com Django 4.2, Celery, Twilio e Bootstrap.
Licença MIT — pode usar, adaptar e arrasar 💃

💅 Frases prontas no sistema

“🧠 Esqueceu do teste de segurança, gata.”

“👏👏 Isso! Agendamento confirmado. Faltam XX dias pro seu momento de beleza.”

“💤 Domingo é dia de descanso, amor.”

“🚫 Já tem uma cliente marcada nesse horário, miga!”

“💅 É hoje, poderosa!”

🌸 Resumo rápido (pra colar na agenda):
Ação	Comando
Criar migrações	python manage.py makemigrations
Aplicar migrações	python manage.py migrate
Rodar local	python manage.py runserver
Rodar Celery	celery -A anna_beauty worker -l info
Criar superusuário	python manage.py createsuperuser
