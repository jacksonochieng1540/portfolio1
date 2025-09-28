from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Experience
from django.contrib.auth.models import User
from datetime import date

class Command(BaseCommand):
    help = 'Setup initial portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Setting up portfolio data...')
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created admin user: admin/admin123'))

        # Create profile
        profile, created = Profile.objects.get_or_create(
            name='John Doe',
            defaults={
                'tagline': 'Full Stack Developer & UI/UX Designer',
                'bio': 'Passionate developer with 5+ years of experience creating modern web applications and user experiences. I love turning complex problems into simple, beautiful, and intuitive solutions.',
                'email': 'john.doe@example.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA',
                'github_url': 'https://github.com/johndoe',
                'linkedin_url': 'https://linkedin.com/in/johndoe',
                'twitter_url': 'https://twitter.com/johndoe',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created profile for John Doe'))

        # Create skills
        skills_data = [
            {'name': 'Python', 'level': 90, 'icon': 'fab fa-python', 'category': 'Backend'},
            {'name': 'Django', 'level': 85, 'icon': 'fas fa-code', 'category': 'Backend'},
            {'name': 'JavaScript', 'level': 88, 'icon': 'fab fa-js-square', 'category': 'Frontend'},
            {'name': 'React', 'level': 80, 'icon': 'fab fa-react', 'category': 'Frontend'},
            {'name': 'HTML/CSS', 'level': 95, 'icon': 'fab fa-html5', 'category': 'Frontend'},
            {'name': 'PostgreSQL', 'level': 75, 'icon': 'fas fa-database', 'category': 'Database'},
            {'name': 'Docker', 'level': 70, 'icon': 'fab fa-docker', 'category': 'DevOps'},
            {'name': 'Git', 'level': 85, 'icon': 'fab fa-git-alt', 'category': 'Tools'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created skill: {skill.name}')

        # Create sample projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'short_description': 'A modern e-commerce platform built with Django and React',
                'description': 'Full-featured e-commerce platform with user authentication, product catalog, shopping cart, payment integration, and admin dashboard. Built with Django REST API backend and React frontend.',
                'featured': True,
                'github_url': 'https://github.com/johndoe/ecommerce-platform',
                'live_url': 'https://demo-ecommerce.com',
            },
            {
                'title': 'Task Management App',
                'short_description': 'A collaborative task management application with real-time updates',
                'description': 'Team collaboration tool with real-time updates, drag-and-drop interface, file attachments, and project analytics. Features include user roles, notifications, and reporting.',
                'featured': True,
                'github_url': 'https://github.com/johndoe/task-manager',
                'live_url': 'https://taskmanager-demo.com',
            },
            {
                'title': 'Portfolio Website',
                'short_description': 'Personal portfolio website with modern design and animations',
                'description': 'Responsive portfolio website built with Django and modern CSS. Features include project showcase, skills visualization, contact form, and blog functionality.',
                'featured': True,
                'github_url': 'https://github.com/johndoe/portfolio',
                'live_url': 'https://johndoe-portfolio.com',
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                # Add some technologies to the project
                python_skill = Skill.objects.filter(name='Python').first()
                django_skill = Skill.objects.filter(name='Django').first()
                js_skill = Skill.objects.filter(name='JavaScript').first()
                
                if python_skill:
                    project.technologies.add(python_skill)
                if django_skill:
                    project.technologies.add(django_skill)
                if js_skill:
                    project.technologies.add(js_skill)
                    
                self.stdout.write(f'Created project: {project.title}')

        # Create sample experience
        experiences_data = [
            {
                'company': 'Tech Innovations Inc.',
                'position': 'Senior Full Stack Developer',
                'description': 'Led development of multiple web applications using Django and React. Managed a team of 3 developers and implemented CI/CD pipelines.',
                'start_date': date(2021, 1, 1),
                'end_date': None,
                'current': True,
            },
            {
                'company': 'StartupXYZ',
                'position': 'Frontend Developer',
                'description': 'Developed responsive web applications using React and modern CSS. Collaborated with designers to implement pixel-perfect UI components.',
                'start_date': date(2019, 6, 1),
                'end_date': date(2020, 12, 31),
                'current': False,
            },
            {
                'company': 'WebSolutions LLC',
                'position': 'Junior Developer',
                'description': 'Built websites using HTML, CSS, JavaScript, and PHP. Learned modern development practices and agile methodologies.',
                'start_date': date(2018, 3, 1),
                'end_date': date(2019, 5, 31),
                'current': False,
            },
        ]
        
        for exp_data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created experience: {experience.position} at {experience.company}')

        self.stdout.write(
            self.style.SUCCESS('Portfolio setup completed successfully!')
        )
        self.stdout.write('You can now run the server and visit /admin to manage your portfolio.')
        self.stdout.write('Admin credentials: admin / admin123')