# Digi Store

[Live Website](https://digi-store-pp5-4acfa738d458.herokuapp.com/)  
[Repository](https://github.com/collinsevan/DigiStore-PP5)

DigiStore is a full stack Django e-commerce application built for users to browse and purchase digital products online. The store focuses on digital downloads rather than physical goods, offering categories such as software, productivity tools, digital art, and audio books through a clean, responsive shopping experience. Users can browse products, view product details, add items to their bag, register for an account, and complete purchases through Stripe, while store owners can manage products and site content through the admin features.

---

## Responsiveness

The site was designed to provide a consistent shopping experience across desktop, tablet, and mobile devices. Responsive layout decisions were applied throughout the project to ensure that navigation, product browsing, product detail pages, bag functionality, and checkout remain clear and usable on different screen sizes.

<p align="center">
  <img src="assets/readme/Screenshot%202026-04-13%20215101.png" alt="Digi Store responsive mockup" width="700">
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
  <img src="assets/readme/Screenshot%202026-04-13%20224218.png" alt="DigiStore homepage overview" width="700">
</p>

### Strategy

The strategy behind DigiStore was to create a digital-only e-commerce store with a clear and familiar shopping flow. The application was designed so that users can land on the homepage, understand the purpose of the site quickly, move into the catalogue, explore products, and complete purchases with as little friction as possible.

A key part of the project strategy was to organise the store around clear digital product categories. This makes the site easier to understand and improves product discovery for users who want to browse software, productivity tools, digital art, and audio books in a structured way.

Another strategic goal was to support both customer and store-owner needs within the same application. Customers can browse and purchase products, while the store owner can manage the catalogue and review product suggestions through dedicated product management views.

<p align="center">
  <img src="assets/readme/Screenshot%202026-04-13%20224320.png" alt="DigiStore products overview" width="700">
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
  <img src="assets/readme/Screenshot%202026-04-13%20224416.png" alt="DigiStore product detail page" width="31%">
  <img src="assets/readme/Screenshot%202026-04-13%20224429.png" alt="DigiStore shopping bag page" width="31%">
  <img src="assets/readme/Screenshot%202026-04-13%20224448.png" alt="DigiStore checkout page" width="31%">
</p>

<p align="center">
  <img src="assets/readme/Screenshot%202026-04-13%20224613.png" alt="DigiStore product suggestion form in profile" width="700">
</p>

### Site Owner Goals

The main site owner goals were to create a professional digital storefront while also making it practical to manage products behind the scenes. As well as providing a customer-facing catalogue and purchase flow, DigiStore was built to support core store administration tasks.

These goals included allowing the store owner to add new products, update existing products, delete products when needed, and manage product suggestions submitted by users. This helps keep the catalogue current and makes the store feel more complete as an e-commerce project.

The product management area was designed to act as a central hub for these actions, making it easier for the store owner to maintain the site without relying only on the Django admin panel.

<p align="center">
  <img src="assets/readme/Screenshot%202026-04-13%20224504.png" alt="DigiStore product management page" width="31%">
  <img src="assets/readme/Screenshot%202026-04-13%20224522.png" alt="DigiStore add product page" width="31%">
  <img src="assets/readme/Screenshot%202026-04-13%20224541.png" alt="DigiStore edit product selection page" width="31%">
</p>

<p align="center">
  <img src="assets/readme/Screenshot%202026-04-13%20224638.png" alt="DigiStore admin product suggestions area" width="700">
</p>

### User Stories

The project was planned using GitHub Projects and user stories to guide development. This helped break the build into manageable tasks and ensured that both user-facing and admin-facing features were planned with purpose.

The board below shows completed work such as user registration, login and logout, browsing products by category, checkout with Stripe, viewing product details, adding products to cart, product suggestions, and admin product management features.

<p align="center">
  <img src="assets/readme/Screenshot%202026-04-13%20230359.png" alt="DigiStore GitHub user stories board" width="700">
</p>

### Database Structure

DigiStore uses a relational database structure to support product browsing, user accounts, checkout functionality, and product suggestion management.

The database design includes models for products and categories, user profile information, orders and line items, and product suggestions. These relationships allow the store to support both customer shopping functionality and store-owner management features.

An ERD for the project will be included below.

### Design

The design of DigiStore focuses on a clean, modern, and professional e-commerce layout. A dark header and footer are used to frame the site, while light content areas improve readability and make product information easier to scan.

The homepage uses a visually stronger hero section to immediately communicate that DigiStore is a digital storefront. Across the rest of the site, the layout becomes more neutral and content-focused so that product cards, forms, and checkout information remain easy to read.

The overall design was kept simple so users could focus on browsing, selecting, and purchasing products without unnecessary distractions. Consistent button styles, spacing, and typography were used throughout the site to support a cohesive experience.

<p align="center">
  <img src="assets/readme/Screenshot%202026-04-13%20224218.png" alt="DigiStore homepage design" width="48%">
  <img src="assets/readme/Screenshot%202026-04-13%20224320.png" alt="DigiStore catalogue design" width="48%">
</p>

---

## SEO and Marketing

---

## Testing

---

## Bugs

---

## Existing Features

---

## Features Left to Implement

---

## Languages, Technologies and Libraries

---

## Credits

---

## Deployment

---

## Acknowledgements
