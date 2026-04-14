# Digi Store

[Live Website](https://digi-store-pp5-4acfa738d458.herokuapp.com/)  
[Repository](https://github.com/collinsevan/DigiStore-PP5)

DigiStore is a full stack Django e-commerce application built for users to browse and purchase digital products online. The store focuses on digital downloads rather than physical goods, offering categories such as software, productivity tools, digital art, and audio books through a clean, responsive shopping experience. Users can browse products, view product details, add items to their bag, register for an account, and complete purchases through Stripe, while store owners can manage products and site content through the admin features.

---

## Responsiveness

The site was designed to provide a consistent shopping experience across desktop, tablet, and mobile devices. Responsive layout decisions were applied throughout the project to ensure that navigation, product browsing, product detail pages, bag functionality, and checkout remain clear and usable on different screen sizes.

<p align="center">
  <img src="assets/readme/responsive-mockup.png" alt="Digi Store responsive mockup" width="700">
</p>

---

## Contents

- [Responsiveness](#responsiveness)
- [UX](#ux)
  - [Project Overview](#project-overview)
  - [Strategy](#strategy)
  - [Target Audience](#target-audience)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Stories](#user-stories)
  - [Database Structure](#database-structure)
  - [Design](#design)
- [SEO and Marketing](#seo-and-marketing)
- [Testing](#testing)
- [Bugs](#bugs)
- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)
- [Languages, Technologies and Libraries](#languages-technologies-and-libraries)
- [Credits](#credits)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

---

## UX

### Project Overview

DigiStore is a full stack Django e-commerce application built as a digital-only online store. The project was created to provide users with a simple and secure way to browse and purchase digital products online through a clean and responsive interface.

Unlike a traditional e-commerce website, DigiStore focuses entirely on digital products rather than physical items. The store is designed around downloadable product categories including software, productivity tools, digital art, and audio books, making it easy for users to browse a varied catalogue of digital content in one place.

The site allows users to search the catalogue, browse products by category, view individual product details, add items to their bag, and complete purchases through Stripe. Authenticated users can also register for an account, access profile features, and interact with product suggestion features, helping to create a smoother experience for returning customers.

From the business side, DigiStore also provides product management features for the store owner, including the ability to add, edit, and delete products, as well as review product suggestions submitted by users. This supports both customer usability and practical store administration within the same application.

The project was developed as Portfolio Project 5 for the Code Institute Full Stack Software Development Diploma and was designed to demonstrate full stack development skills, relational database design, CRUD functionality, responsive design, payment integration, and e-commerce best practices.

<p align="center">
  <img src="assets/readme/homepage-overview.png" alt="DigiStore homepage overview" width="700">
</p>

### Strategy

The strategy behind DigiStore was to create a digital-only e-commerce store with a clear and familiar shopping flow. The application was designed so that users can land on the homepage, understand the purpose of the site quickly, move into the catalogue, explore products, and complete purchases with as little friction as possible.

A key part of the project strategy was to organise the store around clear digital product categories. This makes the site easier to understand and improves product discovery for users who want to browse software, productivity tools, digital art, and audio books in a structured way.

Another strategic goal was to support both customer and store-owner needs within the same application. Customers can browse and purchase products, while the store owner can manage the catalogue and review product suggestions through dedicated product management views.

<p align="center">
  <img src="assets/readme/products-overview.png" alt="DigiStore products overview" width="700">
</p>

### Target Audience

DigiStore is aimed at users who want a simple way to browse and purchase digital products online. The target audience includes customers looking for downloadable products such as audio books, digital art, software, and productivity tools.

The site is also intended for users who value a clean and straightforward shopping experience, including clear navigation, visible product categories, easy-to-use product pages, and a familiar bag and checkout flow.

From a business perspective, the application is also designed for a store owner who needs practical product management features in order to maintain the catalogue and respond to user interest through product suggestions.

### User Goals

The main user goals for DigiStore were:

- to understand the purpose of the site immediately on arrival
- to browse products quickly and clearly
- to search and filter products with ease
- to view product details before purchasing
- to add products to a shopping bag and proceed to checkout
- to create an account and use profile features
- to submit product suggestions for future store additions

Users can achieve these goals through a clear product detail page, a familiar shopping bag layout, and a secure checkout process.

<p align="center">
  <img src="assets/readme/product-detail.png" alt="DigiStore product detail page" width="31%">
  <img src="assets/readme/shopping-bag.png" alt="DigiStore shopping bag page" width="31%">
  <img src="assets/readme/checkout-page.png" alt="DigiStore checkout page" width="31%">
</p>

<p align="center">
  <img src="assets/readme/product-suggestion-form.png" alt="DigiStore product suggestion form in profile" width="700">
</p>

### Site Owner Goals

The main site owner goals were to create a professional digital storefront while also making it practical to manage products behind the scenes. As well as providing a customer-facing catalogue and purchase flow, DigiStore was built to support core store administration tasks.

These goals included allowing the store owner to add new products, update existing products, delete products when needed, and manage product suggestions submitted by users. This helps keep the catalogue current and makes the store feel more complete as an e-commerce project.

The product management area was designed to act as a central hub for these actions, making it easier for the store owner to maintain the site without relying only on the Django admin panel.

<p align="center">
  <img src="assets/readme/product-management.png" alt="DigiStore product management page" width="31%">
  <img src="assets/readme/add-product.png" alt="DigiStore add product page" width="31%">
  <img src="assets/readme/edit-product-select.png" alt="DigiStore edit product selection page" width="31%">
</p>

<p align="center">
  <img src="assets/readme/admin-product-suggestions.png" alt="DigiStore admin product suggestions area" width="700">
</p>

### User Stories

The project was planned using GitHub Projects and user stories to guide development. This helped break the build into manageable tasks and ensured that both user-facing and admin-facing features were planned with purpose.

The board below shows completed work such as user registration, login and logout, browsing products by category, checkout with Stripe, viewing product details, adding products to cart, product suggestions, and admin product management features.

<p align="center">
  <img src="assets/readme/user-stories-board.png" alt="DigiStore GitHub user stories board" width="700">
</p>

### Database Structure

DigiStore uses a relational database structure to support product browsing, user accounts, checkout functionality, and product suggestion management.

The database design includes models for products and categories, user profile information, orders and line items, and product suggestions. These relationships allow the store to support both customer shopping functionality and store-owner management features.

An ERD for the project will be included below.

<p align="center">
  <img src="assets/readme/digistore_erd_clear.png" alt="DigiStore Entity Relationship Diagram" width="800">
</p>

### Design

The design of DigiStore focuses on a clean, modern, and professional e-commerce layout. A dark header and footer are used to frame the site, while light content areas improve readability and make product information easier to scan.

The homepage uses a visually stronger hero section to immediately communicate that DigiStore is a digital storefront. Across the rest of the site, the layout becomes more neutral and content-focused so that product cards, forms, and checkout information remain easy to read.

The overall design was kept simple so users could focus on browsing, selecting, and purchasing products without unnecessary distractions. Consistent button styles, spacing, and typography were used throughout the site to support a cohesive experience.

<p align="center">
  <img src="assets/readme/homepage-overview.png" alt="DigiStore homepage design" width="48%">
  <img src="assets/readme/products-overview.png" alt="DigiStore catalogue design" width="48%">
</p>

### Wireframes

Low-fidelity wireframes were used to plan the main layout patterns of DigiStore before and during development. The aim was to keep the structure clear and user-focused, with familiar e-commerce conventions such as a consistent header, visible navigation, product-first content areas, and a simple purchase flow.

The homepage wireframe focused on introducing the store clearly, using a strong hero area, a call to action, and supporting sections to guide users into browsing the catalogue.

<p align="center">
  <img src="assets/readme/digistore_wireframe_homepage.png" alt="DigiStore homepage wireframe" width="700">
</p>

The products page wireframe was designed around a clear browsing experience, with category context, sorting controls, and a responsive product card grid that allows users to scan multiple items quickly.

<p align="center">
  <img src="assets/readme/digistore_wireframe_products.png" alt="DigiStore products page wireframe" width="700">
</p>

The product detail and management wireframe shows the clean single-page structure used for product information and action-focused layouts. This same pattern also supports store owner flows such as add product, edit product, and suggestion review pages.

<p align="center">
  <img src="assets/readme/digistore_wireframe_detail.png" alt="DigiStore product detail and admin wireframe" width="700">
</p>

### Colour Scheme

The DigiStore colour scheme was designed to create a clean and professional e-commerce experience with strong contrast between key layout areas.

A dark header and footer are used to frame the site and strengthen branding, while light content backgrounds help product information, forms, and page content remain easy to read. This balance supports both visual clarity and a more polished storefront appearance.

Neutral tones are used throughout the main interface, with darker button styles for primary actions and lighter backgrounds for product cards, forms, and general content areas. Accent colours are used more sparingly for hover states, feedback styling, and interactive elements so that the interface remains clear without becoming visually cluttered.

This approach was chosen to keep the focus on the digital products themselves while still giving the site a distinctive and consistent look across the homepage, product pages, profile area, and product management sections.

The main colours used in the project include:

- `#1F2937` for the main header background
- `#111827` for the footer background
- `#FFFFFF` for page backgrounds and card areas
- `#2B2B2B` for hover states and darker button interactions
- `#93C5FD` for accent hover highlights
- `#6C757D` for muted text and supporting copy

<p align="center">
  <img src="assets/readme/colour-palette.png" alt="DigiStore colour palette" width="700">
</p>
---

## SEO and Marketing

### SEO

Search engine optimisation was implemented to improve the visibility, structure, and crawlability of the DigiStore website. The project uses a combination of technical SEO foundations and on-page content improvements to help search engines understand the purpose of the site and its individual pages.

A reusable SEO structure was added through the base template, including meta description and meta keyword blocks, as well as canonical links. This allows the site to provide a default SEO foundation across pages while also supporting more specific SEO content on key templates such as the products page and product detail pages.

The products page includes targeted copy describing the digital catalogue, while individual product detail pages generate more specific meta content based on the product being viewed. This helps make category and product pages more relevant to search intent and supports better page indexing.

Technical SEO was also implemented through a live `robots.txt` file and a working `sitemap.xml`, helping search engines crawl the website more effectively. The sitemap includes important site URLs and product pages, while the robots file directs crawlers to the sitemap location.

<p align="center">
  <img src="assets/readme/robots-txt.png" alt="DigiStore robots.txt file" width="700">
</p>

<p align="center">
  <img src="assets/readme/sitemap-xml.png" alt="DigiStore sitemap.xml file" width="700">
</p>

The screenshots below show the main catalogue and homepage content that support keyword targeting and page relevance for search engines.

<p align="center">
  <img src="assets/readme/homepage-overview.png" alt="DigiStore homepage SEO content" width="48%">
  <img src="assets/readme/products-overview.png" alt="DigiStore products page SEO content" width="48%">
</p>

### Marketing

The marketing approach for DigiStore was planned around presenting the business as a digital-only online store with a clear and focused niche. The project targets users looking for downloadable products such as software, productivity tools, digital art, and audio books, and the content across the site reflects those product types consistently.

The homepage was designed to communicate the store purpose immediately through a clear headline, supporting copy, and a direct call to action. Product categories are also visible in the main navigation, helping guide users toward relevant sections of the store quickly and supporting both usability and discoverability.

A Facebook business mockup was planned as part of the project marketing materials and will be added to this section. This was intended to represent how the brand could be promoted through social media in a realistic e-commerce context.

Newsletter marketing was also considered as part of the wider promotional strategy for encouraging repeat visits and future customer engagement.

---

## Testing

---

## Bugs

---

## Existing Features

DigiStore includes a range of user-facing and store-owner features designed to create a complete digital e-commerce experience.

### General Site Features

- Responsive layout designed for desktop, tablet, and mobile browsing
- Consistent header, navigation, and footer structure across the site
- Homepage hero section with clear store messaging and a call to action
- Product-focused layout designed to keep browsing and purchasing straightforward
- Back to top functionality in the footer
- Social media links in the footer
- Clear visual hierarchy through consistent spacing, typography, and button styling

### User Account Features

- User registration through Django Allauth
- User login and logout functionality
- Profile area for authenticated users
- Automatic user profile creation when a user account is created
- Saved default user information through the user profile model
- Order history available through the user profile section

### Product Browsing Features

- Dedicated products page displaying the full digital catalogue
- Category-based browsing for:
  - Audio Books
  - Digital Art
  - Productivity
  - Software
- Search functionality for product names and descriptions
- Product sorting options, including:
  - Price
  - Category
  - Name
- Product detail pages with:
  - Product image
  - Product title
  - Price
  - Description
  - Quantity selector
  - Add to bag functionality
  - Keep shopping action

### Bag and Checkout Features

- Shopping bag page showing selected items
- Quantity adjustment controls inside the bag
- Remove item functionality
- Bag total calculation
- Stripe checkout integration
- Order summary shown during checkout
- Save information option for returning authenticated users
- Order creation and storage after successful payment
- Order line item storage linked to products and orders
- Unique order reference generation
- Order totals calculated automatically from line items
- Stripe webhook handling for successful and failed payments
- Order confirmation email workflow

### Product Suggestion Features

- Authenticated users can submit product suggestions
- Suggestion form allows users to provide:
  - Suggested product name
  - Suggested category
  - Description
  - Reason
  - Optional reference URL
- Users can view their own product suggestion area within the profile page
- Suggestions provide a useful interaction feature beyond purchasing

### Store Owner Features

- Superuser-only product management access
- Dedicated product management page for store owners
- Add product form
- Edit product selection page
- Edit product form
- Delete product selection page
- Delete product confirmation page
- Ability to create a product suggestion from the management area
- Ability to review submitted product suggestions
- Ability to edit product suggestions
- Ability to delete product suggestions
- Ability to create a product directly from an approved suggestion
- Prefilled product creation flow from suggestions
- Automatic suggestion status updates when a suggestion is used to create a product

### Database Features

- Interrelated relational database structure using Django models
- Categories linked to products
- User profiles linked to authenticated users
- Orders linked to user profiles
- Order line items linked to both orders and products
- Product suggestions linked to authenticated users
- Automatic profile creation and update through signals
- Automatic order total recalculation when line items are created or removed

### SEO Features

- Reusable meta description block in the base template
- Reusable meta keywords block in the base template
- Canonical links added through the base template
- SEO-focused homepage and product catalogue copy
- Product-specific meta description and keyword support on product detail pages
- Working `robots.txt`
- Working `sitemap.xml`

### Design and UX Features

- Clean and consistent colour palette
- Strong homepage hero section for first impressions
- Product cards designed for easy scanning
- Form layouts kept simple and readable
- Consistent button styling throughout the site
- Clear separation between customer-facing flows and store-owner management flows

---

## Features Left to Implement

Although DigiStore includes the core functionality required for a digital e-commerce project, there are still several features that could be added in future development to expand the user experience and business value of the site.

### Wishlist Functionality

A wishlist feature would allow users to save products they are interested in without adding them to the shopping bag immediately. This would improve the browsing experience for returning users and create a stronger link between discovery and later purchase.

### Product Reviews

Customer reviews would provide social proof and help users make more informed purchasing decisions. Reviews could be restricted to verified purchasers in order to keep feedback relevant and reliable.

### Promo Codes and Discounts

A promotional code feature would allow the store owner to run seasonal promotions, encourage repeat purchases, and support marketing campaigns. This would also make the project feel even closer to a real-world e-commerce platform.

### Gift Card or Store Credit Functionality

A gift card or digital credit feature would expand the business model and create more flexibility for users. This could be especially useful in a digital store where purchases are quick and fulfilment is immediate.

### Newsletter Signup Integration

Newsletter marketing was considered as part of the wider marketing strategy, and a future version of the site could include a fully connected newsletter signup flow. This could support customer retention, product launches, and promotional campaigns.

### Facebook Business Integration

A stronger social media presence could be supported by expanding the current marketing assets into a fuller Facebook business strategy, including post examples, promotional content, and campaign planning.

### Enhanced Filtering

The site currently supports search, category browsing, and sorting, but could be extended with more advanced filtering options such as price range, rating, or licence type. This would improve usability as the catalogue grows.

### Improved Product Suggestion Workflow

The product suggestion system is already functional, but future improvements could include:
- suggestion status filtering
- richer moderation tools
- suggestion approval notifications
- clearer user feedback on suggestion outcomes

### Digital Delivery Enhancements

As DigiStore is a digital-only store, future development could introduce more advanced digital fulfilment features such as downloadable file delivery, secure access limits, or digital licence delivery workflows. These features were outside the current project scope but would be valuable in a production-ready version.

### Enhanced Admin Reporting

The store owner area could be expanded with reporting features such as:
- best-selling products
- recent orders overview
- revenue summaries
- product performance by category

### Improved Customer Communication

Future versions could include stronger customer communication features such as:
- better order confirmation messaging
- profile notifications
- suggestion response messages
- promotional email flows

### Additional Accessibility Improvements

The project was built with usability in mind, but accessibility could be improved further over time through expanded testing and refinement, including:
- deeper keyboard navigation testing
- more detailed screen reader checks
- further accessibility audits across forms and interactive components

---

## Languages, Technologies and Libraries

DigiStore was built using a range of languages, frameworks, libraries, and supporting tools to create a full stack Django e-commerce application.

### Languages Used

- **HTML5**  
  Used to structure the site templates and page content.

- **CSS3**  
  Used to style the layout, components, responsive behaviour, colour scheme, and overall presentation of the site.

- **JavaScript**  
  Used for interactive front-end behaviour such as UI enhancements, sorting behaviour, image upload feedback, toast display, and back to top interaction.

- **Python**  
  Used for the server-side application logic, model definitions, views, forms, checkout workflow, and webhook handling.

### Frameworks and Libraries

- **Django**  
  The main Python web framework used to build the project, manage routing, models, views, forms, templates, authentication, and admin functionality.

- **Bootstrap 4**  
  Used for responsive layout, grid structure, spacing utilities, buttons, forms, navigation, and general front-end styling support.

- **jQuery**  
  Used to support interactive UI behaviour such as sorting controls, back to top functionality, image upload filename display, and toast handling.

- **Django Allauth**  
  Used to manage user registration, login, logout, and account-related authentication flows.

- **Django Crispy Forms**  
  Used to render forms in a cleaner and more consistent way across the project.

- **Font Awesome**  
  Used for icons in the navigation, footer, account actions, search, bag, and other interface elements.

- **Google Fonts**  
  Used to load the Lato font family for the site’s typography.

- **Stripe**  
  Used for payment processing and checkout integration.

### Database and Data Handling

- **SQLite**  
  Used as the local development database.

- **PostgreSQL**  
  Used for the deployed production database environment.

### Storage, Deployment and Hosting

- **Heroku**  
  Used to deploy and host the live DigiStore application.

- **AWS / cloud storage setup**  
  Used for media and static asset handling in the deployed environment.

### Development Tools

- **Git**  
  Used for version control throughout the project.

- **GitHub**  
  Used to host the repository, manage commits, track development progress, and document user stories through GitHub Projects.

- **VS Code**  
  Used as the main development environment.

- **GitHub Projects / Kanban board**  
  Used to plan and manage the project using user stories and task tracking.

### Project Features Supported by These Technologies

These technologies were used together to support:

- user authentication
- relational database modelling
- digital product browsing
- shopping bag functionality
- Stripe checkout processing
- order storage and history
- product management CRUD functionality
- product suggestion workflows
- responsive design
- SEO implementation
- deployment and version control

Overall, the chosen stack supported the creation of a practical digital e-commerce application while also demonstrating the full stack development skills required for the project.

---

## Credits

---

## Deployment

---

## Acknowledgements
